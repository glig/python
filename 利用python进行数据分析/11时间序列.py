# 如何标记和引用时间序列数据取决于应用程序，并且您可能有以下其中一项：
# · 时间戳，具体的时刻。
# · 固定的时间区间，例如2007的1月或整个2010年。
# · 时间间隔，由开始和结束时间戳表示。时间区间可以被认为是间隔的特殊情况。
# · 实验时间或消耗时间。每个时间戳是相对于特定开始时间的时间的量度（例如，自从被放置在烤箱中每秒烘烤的饼干的直径）。

# 11.1 日期和时间数据的类型及工具
# datetime、time和calendar模块是开始处理时间数据的主要内容。datetime.datetime类型，或简写为datetime，是广泛使用的：

from datetime import datetime
from datetime import timedelta

import pandas as pd
from dateutil.parser import parse
import numpy as np
now=datetime.now()
# 返回当前时间
now.year,now.month,now.day

# delta返回当前的时间差
delta=datetime(2011,1,1)-datetime(2008,6,24,8,15)
# 920 days, 15:45:00
delta.days  #926
delta.seconds  #56700

# 你可以为一个datetime对象加上（或减去）一个timedelta或其整数倍来产生一个新的datetime对象：
start=datetime(2011,1,7)
start+timedelta(12)  #2011-01-19 00:00:00
start-2*timedelta(12) #2010-12-14 00:00:00

# 11.1.1 字符串与datetime互相转换
stamp=datetime(2011,1,3)
str(stamp) #2011-01-03 00:00:00
stamp.strftime('%Y-%m-%d')  #2011-01-03

# 你可以使用datetime.srtptime和这些格式代码，将字符串转换日期：
value='2011-01-03'
datetime.strptime(value,'%Y-%m-%d')                   #2011-01-03 00:00:00
datestrs=['7/6/2011','8/6/2011']
[datetime.strptime(x,'%m/%d/%Y') for x in datestrs]   #[datetime.datetime(2011, 7, 6, 0, 0), datetime.datetime(2011, 8, 6, 0, 0)]

# datetime.strptime是在已知格式的情况下转换日期的好方式。然而，每次都必须编写一个格式代码可能有点烦人，特别是对于通用日期格式。
# 在这种情况下，你可以使用第三方dateutil包的parser.parse方法（这个包在安装pandas时已经自动安装）
parse('2011-01-03')               #datetime.datetime(2011,1,3,0,0)
# dateutil能够解析大部分分类可以理解的日期表示
parse('Jan 31,1997 10:45 PM')     #datetime.datetime(1997,1,31,22,45)
# 在国际场合下，日期出现在月份之前很常见，因此你可以传递dayfirst=True来表明这种情况：
parse('6/12/2011',dayfirst=True)

# pandas主要是面向处理日期数组的，无论是用作轴索引还是用作DataFrame中的列。to_datetime方法可以转换很多不同的日期表示格式
datestrs=['2011-07-06 12:00:00','2011-08-06 00:00:00']
pd.to_datetime(datestrs)       #DatetimeIndex(['2011-07-06 12:00:00', '2011-08-06 00:00:00'], dtype='datetime64[ns]', freq=None)

# to_datetime方法还可以处理那些被认为是缺失值的值(None,空字符串)
idx=pd.to_datetime(datestrs+[None])  #DatetimeIndex(['2011-07-06 12:00:00', '2011-08-06 00:00:00', 'NaT'], dtype='datetime64[ns]', freq=None)
idx[2]   # NaT  NaT（Not a time）是pandas中时间戳数据的是null值。
pd.isnull(idx)    #[False False  True]

# 11.2时间序列基础
# pandas中的基础时间序列种类是由时间戳索引的Series，在pandas外部则通常表示为Python字符串或datetime对象：
dates=[datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),
       datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
ts=pd.Series(np.random.randn(6),index=dates)
# 2011-01-02   -0.462862
# 2011-01-05    1.882044
# 2011-01-07    0.222464
# 2011-01-08   -1.332894
# 2011-01-10   -0.983783
# 2011-01-12   -0.169395
# dtype: float64

# 这种情况下这些datetime对象可以被放入DatetimeIndex中：



print(ts)