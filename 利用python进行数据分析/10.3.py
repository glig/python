#应用：通用拆分-应用-联合
# apply将对象拆分成多块，然后在每一块上调用传递的函数，之后尝试将每一块拼接到一起
import numpy as np
import pandas as pd
import statsmodels.api as sm
tips = pd.read_csv('examples/tips.csv')
# 在读取小费的DataFrame中添加tip_pic列值为tip列减去total_bill列。
tips['tip_pct'] = tips['tip'] / tips['total_bill']

# 显示在tip_pct列中，倒数n个最大值，
def top(df,n=5,column='tip_pct'):
    return df.sort_values(by=column)[-n:]
top(tips,n=6)
# 将tips按照smoker进行分组，并在每组上调用top函数，并使用pandas.contact将结果粘贴在一起，并使用分组名作为各组的标签，
# 结果是一个分层索引，该分层索引的内部层级包含员DataFrame的索引值
result=tips.groupby('smoker').apply(top)
# 通过函数的参数传参并增加分组参数，获取是否抽烟中每一天的倒序一个最大值
result=tips.groupby(['smoker','day']).apply(top,n=1,column='total_bill')
# DataFrame groupBy的describe的描述性统计结果
result=tips.groupby('smoker')['tip_pct'].describe()
#转换为Series形式，根据列名进行分类。（stack根据index标签进行分类。）
result.unstack('smoker')

# 10.3.1压缩分组键
# 通过向groupby传递group_keys=False来禁用具有分组键所形成的分层索引及每个原色对象的索引
tips.groupby('smoker',group_keys=False).apply(top)

#10.3.2分位数与桶分析
# 第八章pandas的cut和qcut，将数据按照你选择的箱位或者样本分位数进行分桶。可以与pandas一起使用这些函数方便的进行分桶或者分位分析。
# 对data1进行分箱操作分为4组
frame=pd.DataFrame({'data1':np.random.randn(1000),
                    'data2':np.random.randn(1000)})
quartiles=pd.cut(frame.data1,4)
quartiles[:10]

# 分箱后的Categorical对象（分箱每个箱的区间）可以直接传给groupby。所以可计算出data2列的一个统计值集合,这些集合就是等长桶
def get_stats(group):
    return{'min':group.min(),'max':group.max(),'count':group.count(),'mean':group.mean()}
grouped=frame.data2.groupby(quartiles)
grouped.apply(get_stats).unstack()

# 为了根据样本分位数计算出等大小的桶，则需要使用qcut.通过传递labels=False来获得分位数数值
# 返回分位数数值
grouping=pd.qcut(frame.data1,10,labels=False)
grouped=frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()

# 10.3.3 示例：使用指定分组值填充缺失值
#使用fillna将NAN值填充为其他值
s=pd.Series(np.random.randn(6))
# 各两个赋值nan
s[::2]=np.nan
s.fillna(s.mean())

# 使填充值按照组来变化
states=['Ohio','NewYork','Vermont','Florida','Oregon','Nevada','California','Idaho']
group_key=['East']*4+['West']*4
data=pd.Series(np.random.randn(8),index=states)
data[['Vermont','Nevada','Idaho']]=np.nan
# data与group_key都是8个，默认将列表拼接在一起
data.groupby(group_key).mean()
# 定义匿名函数用所调用变量的平均值来填充对象，注意已经将data进行分组，填充的是每一个组的平均数
fill_mean=lambda g:g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)



# 已经为每个分组预定义了填充值，由于每个分组都有一个内置的name属性，我们可以这样使用
fill_values={'East':0.5,'West':-1}
fill_func= lambda g:g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)


#10.3.4 示例：随机采样与排列
# 红桃、黑桃、梅花、方块
suit=['H','S','C','D']
# 得到列表car_val范围1-10加上3个10，“1……10，10，10，10”共四组
card_val=(list(range(1,11))+[10]*3)*4
# 得到牌的名字A，1，2,……J，K，Q
base_name=['A']+list(range(2,11))+['J','K','Q']
# 将base_name中的值转换为字符串+suit，“AH……QD”
cards=[]
for suit in['H','S','C','D']:
    cards.extend(str(num)+suit for num in base_name)
#形成Series,将纸牌和值进行对应
deck=pd.Series(card_val,index=cards)
# 随机抽取5张牌
def draw(deck,n=5):
    return deck.sample(n)
draw(deck)
# 每组随机抽取两张牌
get_suit=lambda card:card[-1] #得到花色的最后一个字母，用于分组
deck.groupby(get_suit).apply(draw,n=2) #每个组里随机抽取两张
deck.groupby(get_suit,group_keys=False).apply(draw,n=1) #每组随机抽两张的另外一种写法，group_keys不显示默认分组标签



# 10.3.5示例：分组加权平均和相关性
df=pd.DataFrame({'category':['a','a','a','a','b','b','b','b'],
                 'data':np.random.randn(8),
                 'weights':np.random.randn(8)})
grouped=df.groupby('category')
get_wavg=lambda g:np.average(g['data'],weights=g['weights'])
result=grouped.apply(get_wavg)


close_px=pd.read_csv('examples/stock_px.csv',parse_dates=True,index_col=0)
close_px.info()
close_px[-4:]
# 计算每一列与SPX的关联性即相关性
spx_corr=lambda x: x.corrwith(x['SPX'])
# 计算每个元素与前一个元素的百分比的变化，删除缺失值
rets=close_px.pct_change().dropna()
# 按照年对百分比变化进行分组
get_year=lambda x: x.year
by_year=rets.groupby(get_year)
by_year.apply(spx_corr)
# 也可以计算内部相关性，计算苹果和微软的年度相关性
by_year.apply(lambda g: g['AAPL'].corr(g['MSFT']))

# 10.3.6 示例：逐组线性回归
def regresss(data,yvar,xvars):
    y=data[yvar]
    x=data[xvars]
    x['intercept']=1.
    result=sm.OLS(y,x).fit()
    return result.params
by_year.apply(regresss,'AAPL',['SPX'])


print(by_year.apply(regresss,'AAPL',['SPX']))