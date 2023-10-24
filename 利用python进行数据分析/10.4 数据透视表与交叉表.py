# 数据透视表是电子表格程序和其他数据分析软件中常见的数据汇总工具。它根据一个或多个键聚合一张表的数据，将数据在矩形格式中排列，
# 其中一些分组键是沿着行的，另一些是沿着列的。Python中的pandas透视表是通过本章所介绍的groupby工具以及使用分层索引的重塑操作实现的。
# DataFrame拥有一个pivot_table方法，并且还有还一个顶层的pandas.pivot_table函数。除了为groupby提供一个方便接口，
# pivot_table还可以添加部分总计，也称作边距。

import numpy as np
import pandas as pd

tips=pd.read_csv('examples/tips.csv')
tips.pivot_table(index=['day','smoker'])
# tips.to_numeric()
# tips['day'].astype(float)

# print(tips.pivot_table(index="day"))