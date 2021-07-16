import json
import numpy

import pandas as pd
from pandas import DataFrame
filename= 'D:\GitCode\Python\chenff/ages/top10part/age给你呀（又名：for ya）.json'
with open(filename) as file_obj:
    data=json.load(file_obj)
data=pd.Series(data)
c_value=[2021-int(i) for i in data.values]
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
# 处理数据1
#删除异常值
bins=[5, 10, 20, 30, 40, 100]
labels= ['10岁以下', '10~20岁', '20~30岁', '30~40岁', '40岁以上']
result= pd.cut(c_value, bins).value_counts().sort_index()
print(result)
bar=Bar()
bar.add_xaxis(labels)
bar.add_yaxis("粉丝数", [3, 176, 50, 12, 1])
bar.set_global_opts(title_opts=opts.TitleOpts(title="粉丝年龄层分布",subtitle="柱状图"),)
bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=True),
        makepoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_='max', name='最大值'),
                opts.MarkPointItem(type_='min', name='最小值'),
            ]

        ),
        itemstyle_opts=opts.ItemStyleOpts(color='pink')
    )

import pandas
from pyecharts.charts import Map
filename1='D:\GitCode\Python\chenff\locations/top10part\location给你呀（又名：for ya）.json'
with open(filename1) as file_obj:
    data=json.load(file_obj)
data1= pandas.value_counts(data)
print(data1)
del data1['海外']
c_value=[int(i) for i in data1.values]
print(data1.index)
print(c_value)
result=[(a,b) for a,b in zip(data1.index, c_value)]
map= Map()
map.add("粉丝分布地区", result, "china")

from pyecharts.charts import Page
page=Page()
page.add(bar,map)
page.render('给你呀.html')
