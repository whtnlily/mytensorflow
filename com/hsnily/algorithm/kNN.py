#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
from com.hsnily.utils import util
import operator

"""
kNN算法：即k-近邻算法
"""

def createDataSet():
    tgroup = array([[1.0,1.1],[1.0,1.0],[0.0,0.0],[0.0,0.1]])
    tlabels = ['A','A','B','B']
    return tgroup,tlabels

def classify0(inX,dataSet,labels,k):
    # ====1、使用欧式距离公式计算两个向量点之间的距离====
    print('classify0===>用于分类的输入向量inX:')
    util.printData(inX)
    print('classify0===>训练样本集dataSet:')
    util.printData(dataSet)
    print('classify0===>标签向量labesl:')
    util.printData(labels)
    dataSetSize = dataSet.shape[0]   # 矩阵的行数，dataSet.shape = (4,2) => dataSet.shape[0] = 4
    # 获得xA - xB 的矩阵
    print('classify0===>将输入向量扩展为与训练样本一致的矩阵tile(inX,(dataSetSize,1)):')
    util.printData(tile(inX,(dataSetSize,1)))
    diffMat = tile(inX,(dataSetSize,1)) - dataSet   # tile将数组inX复制，并生成新的二维矩阵。复制次数为dataSetSize次
    print('classify0===>标签向量-训练样本后的矩阵diffMat:')
    util.printData(diffMat)
    sqDiffMat = diffMat ** 2
    print('classify0===>元素差的平方：sqDiffMat:')
    util.printData(sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    print('classify0===>所有元素的差的平方和sqDistances:')
    util.printData(sqDistances)
    distances = sqDistances ** 0.5   # 开根号
    print('classify0===>平方和开根号distances:')
    util.printData(distances)
    sortedDistIndicies = distances.argsort()   # argsort函数返回的是数组值从小到大的索引值
    print('classify0===>数组的值从小到大的索引值sortedDistIndicies:')
    util.printData(sortedDistIndicies)

    # ====2、选择距离最小的k个点====
    classCount = {}
    for i in range(k):
        votellabel = labels[sortedDistIndicies[i]]
        classCount[votellabel] = classCount.get(votellabel,0) + 1

    # ====3、排序====
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount

def kNNTest():
    group, labels = createDataSet()
    print('kNNTest===> 训练样本集：')
    util.printData(group)
    print('kNNTest===> 标签向量：')
    util.printData(labels)

    result = classify0([0, 0], group, labels, 3)
    print('kNNTest===> 通过kNN算法后获得的最终结果：')
    util.printData(result)

if __name__ == "__main__":
    kNNTest()