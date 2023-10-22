# pandas.DataFrame.describe  描述性统计结果
# count      分组中的非NA值数量
# sum        非NA值的累积
# mean       非NA值的均值
# median     非NA值的算术中位数
# std、var   无偏的（n-1分母）标准差和方差
# min、max   非NA值的最小值、最大值
# prod       非NA值的乘积
# first、last 非NA值的第一个和最后一个值
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 10.2.1逐列及多函数应用
# 函数peak_to_peak返回参数的最大值减去最小值
def peak_to_peak(arr):
    return arr.max() - arr.min()


# 读取csv文件
tips = pd.read_csv('examples/tips.csv')
# 在读取小费的DataFrame中添加tip_pic列值为tip列减去total_bill列。
tips['tip_pct'] = tips['tip'] / tips['total_bill']

# 通过day和smoker进行分组展示tip_pct
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
# 通过day和smoker进行分组,展示tip_pct的均值，标准差，及函数peak_to_peak的结果
test = grouped_pct.agg(['mean', 'std', peak_to_peak])
# 通过day和smoker进行分组,展示tip_pct的均值，标准差，并修改列名字
test = grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])
# 通过day和smoker进行分组,展示tip_pct和total_bill的总和，均值，及最大数
functions = ['count', 'mean', 'max']
result = grouped[['tip_pct', 'total_bill']].agg(functions)

# 按照day和smoker分组，计算tip_pct和total_bill的平均值和方差，并分别将列明命名为Durchschnitt和Abweichung
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped[['tip_pct', 'total_bill']].agg(ftuples)
# 按照day和smoker分组，计算tip的最大值和size的和，需要将含有列明和函数对应关系的字典传递给agg
result=grouped.agg({'tip':np.max,'size':'sum'})

result=grouped.agg({'tip_pct':['min','max','mean','std'],'size':'sum'})
print(result)
# 10.2.2 返回不含行索引的聚合数据
# as_index=False来禁用分组键作为索引的行为,通过在结果上调用reset_index也可以获得同样的结果。使用as_index=False可以避免一些不必要的计算
tips.groupby(['day','smoker'],as_index=False).mean()
