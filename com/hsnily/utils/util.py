#!/usr/bin/env python
# -*- coding: utf-8 -*-

def printLine():
    print('=================================')


# 打印数据对象
def printData(data):
    print(data)
    printLine()

# 打印迭代对象
def printIterData(idata):
    for d in idata:
        print(d,end=' ')
    print('\n', end='')
    printLine()

