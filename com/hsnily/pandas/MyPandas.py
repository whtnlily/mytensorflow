#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Iterable

__author__ = "hyman.wan"
__date__ = "2018/01/17"
import pandas as pd
from com.hsnily.utils import util
from pandas import Series,DataFrame
import numpy as np

"""
pandas学习笔记
pandas主要的数据结构：
1、Series:类似一维数组的对象，它由一组数据以及一组标记前面数据的标签(即索引)组成。索引在左边，值在右边。
2、DataFrame:是一个表格型的数据结果，它包含一组有序的列，每列可以是不同的值类型。既有行索引也有列索引。它可以被看做是由Series组成的字典。
构建DataFrame的方法有很多，最常用的一种是直接传入一个由等长列表或Numpy数组组成的字典。
"""

dataList = []

# 一 Series对象
# 1.1 创建Series对象
sera = Series([4,7,-5,3])
dataList.append('Series ===> 创建Series对象,不指定索引，默认从0开始')
dataList.append(sera)
dataList.append('Series ===> 获取valus')
dataList.append(sera.values)
dataList.append('Series ===> index')
dataList.append(sera.index)

serb = Series([96,90,70,82],index=['husn','caim','sjj','lyh'])
dataList.append('Series ===> 指定索引的Series对象')
dataList.append(serb)
dataList.append('Series ===> 通过索引获取指定的value')
dataList.append(serb['husn'])
dataList.append('Series ===> 根据条件过滤指定的value')
dataList.append(serb > 80)

dataList.append('Series ===> 通过字典创建Series对象,索引即使字典的键')
dica = {'husn':96,'caim':90,'dingx':92,'gyl':90}
serc = Series(dica)
dataList.append(serc)

# 1.2 Series算术运算
dataList.append('Series ===> 算术运算-原始数据1')
dataList.append(serb)
dataList.append('Series ===> 算术运算-原始数据2')
dataList.append(serc)
dataList.append('Series ===> 算术运算-运算结果,将相同的索引的value相加')
dataList.append(serb+serc)

# 二、DataFrame数据结构
# 2.1 创建DataFrame对象
data = {'name':['husn','liut','huyy','yangxx','gongyl'],
        'score':[96,90,92,85,86],
        'xw':[118.5,75,95.5,98,101]}
framea = DataFrame(data)
dataList.append('dataframe ===> 创建dataframe对象，缺省索引')
dataList.append(framea)

dataList.append('dataframe ===> 创建dataframe对象，指定列排序')
dataList.append(DataFrame(data,columns=['xw','name','score']))

dataList.append('dataframe ===> 创建dataframe对象，根据列名获取一个列Series')
dataList.append(framea['name'])

dataList.append('dataframe.ix ===> 创建dataframe对象，根据索引获取一个行Series')
dataList.append(framea.ix[2])

# 2.2 赋值，为不存在的列赋值会创建出一个新列，为一个存在的列赋值时，长度必须与dataframe的长度匹配
val = Series([97,87,90,86,87])
framea['score'] = val
dataList.append('dataframe ===> 为存在的列赋值，长度必须与dataframe匹配')
dataList.append(framea)

val = Series([130,100.5,116.5,113,117.5])
framea['tw'] = val
dataList.append('dataframe ===> 为不存在的列赋值，则增加一个新列')
dataList.append(framea)

# 2.3 del删除列
del framea['xw']
dataList.append('del ===> 删除一列')
dataList.append(framea)

# 测试函数
def testPandas():

    if len(dataList):
        for data in dataList:
            if isinstance(data,str):  # 如果是字符串，则直接打印
                print(data)
            else:
                # 判断对象是迭代对象，但不是多维数组
                util.printData(data)
                # if isinstance(data, Iterable) and not isinstance(data, pd.Series):
                #     util.printIterData(data)
                # else:
                #     util.printData(data)
    else:
        print("data list is null")

if __name__ == "__main__":
    testPandas()

