#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "hyman.wan"
__date__ = "2018/01/17"
import numpy as np
from collections import Iterable
from com.hsnily.utils import util

'''
本文件为numpy学习笔记
教程参考：https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-1-np-attributes/
numpy主要是矩阵运算。
一、numpy属性：
1.1 array：创建数组
1.2 dtype：指定数据类型
1.3 zeros：创建数据全为0
1.4 ones：创建数据全为1
1.5 empty：创建数据接近0
1.6 arrange：按指定范围创建数据
1.7 linspace：创建线段

二、numpy基础运算
2.1 一维矩阵加减乘除：必须保证两个矩阵形状相同。即矩阵的行数，列数必须一致。
2.2 三角函数
2.3 逻辑运算
2.4 多维矩阵运算
2.5 随机数矩阵
2.6 对矩阵内元素进行运算
2.7 索引
2.8 求矩阵的均值
2.9 获取矩阵中的元素
注：其他运算参见：https://www.cnblogs.com/smallpi/p/4550361.html
    官方文档：https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
'''

dataList = []

# 1.1、将列表转换为矩阵
array = np.array([[1, 2, 3], [4, 5, 6]])
dataList.append("np.array ===> 二维数组")
dataList.append(array)

# 1.2、创建数组,1维
arr = np.array([7, 8, 9])
dataList.append("np.array ===> 一维数组")
dataList.append(arr)

# 1.3、指定数据类型
int64a = np.array([2, 23, 4], dtype=np.int64)
int32a = np.array([2, 23, 4], dtype=np.int32)
float64a = np.array([2, 23, 4], dtype=np.float)
float32a = np.array([2, 23, 4], dtype=np.float32)
dataList.append("np.array ===> 指定类型 dtype=int64")
dataList.append(int64a)
dataList.append("np.array ===> 指定类型 dtype=int32")
dataList.append(int32a)
dataList.append("np.array ===> 指定类型 dtype=float32")
dataList.append(float32a)
dataList.append("np.array ===> 指定类型 dtype=float")
dataList.append(float64a)

# 1.4、创建全0矩阵
aerosa = np.zeros((2, 3))
aerosb = np.zeros((3, 3), dtype=np.complex)
dataList.append("np.zeros ===> 全0矩阵")
dataList.append(aerosa)
dataList.append("np.zeros ===> 指定数据类型的全0矩阵")
dataList.append(aerosb)

# 1.5、创建全1矩阵
onesa = np.ones((3, 2))
onesb = np.ones((2, 2), np.complex)
dataList.append("np.ones ===> 全1矩阵")
dataList.append(onesa)
dataList.append("np.ones ===> 指定数据类型的全1矩阵")
dataList.append(onesb)

# 1.6、创建空矩阵
emptya = np.empty((2, 2))
dataList.append("np.empty ===> 空矩阵")
dataList.append(emptya)

# 1.7、按指定范围创建数据,从2-20之间的数字，步长为3
arrangea = np.arange(2,20,3)
dataList.append("np.arange ===> 指定范围创建一维数组")
dataList.append(arrangea)
# 创建12以内的连续数据，然后将该序列设置为3行4列的矩阵，但必须保证数据个数与矩阵的元素个数一致。
arangeb = np.arange(12).reshape((3,4))
dataList.append("np.reshape ===> 将array一维数组转换为多维矩阵")
dataList.append(arangeb)

# 1.8、创建线段
linea = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
lineb = np.linspace(2,20,10).reshape((5,2))  # 将线段转换成矩阵，必须保证矩阵的元素个数与前面的元素个数一致
dataList.append("np.linespace ===> 创建线段")
dataList.append(linea)
dataList.append("np.reshape ===> 将线段转换为矩阵")
dataList.append(lineb)

# 2.1、矩阵相减
shapea = np.array([10,20,30,40,50])
shapeb = np.arange(5)
shapec = shapea-shapeb
shaped = shapea*shapeb
shapee = shapeb**2    # 平方
dataList.append("- * **===> 矩阵运算原始值a")
dataList.append(shapea)
dataList.append("- * **===> 矩阵运算原始值b")
dataList.append(shapeb)
dataList.append("- * **===> 矩阵运算a-b")
dataList.append(shapec)
dataList.append("- * **===> 矩阵运算a*b")
dataList.append(shaped)
dataList.append("- * **===> 矩阵运算a**b")
dataList.append(shapee)

# 2.2、三角函数
sina = 10*np.sin(shapea)
cosa = 10*np.cos(shapea)
dataList.append("np.sin ===> 三角函数")
dataList.append(sina)
dataList.append("np.cos ===> 三角函数")
dataList.append(cosa)

# 2.3 逻辑运算
yua = shapea > 20
dataList.append("> ===> 逻辑运算")
dataList.append(yua)

# 2.4 多维矩阵运算
sa = np.arange(1,20,2).reshape((5,2))
sb = np.arange(10).reshape((2,5))
sc = np.dot(sa,sb)      # 两个相乘的矩阵要保证行列数互异，即一个矩阵的行列是x * y，另一个矩阵的行列必须是y * x
sd = sa.dot(sb)   # 效果与np.dot()一样
dataList.append("np.dot ===> 多维矩阵相乘原始数据a")
dataList.append(sa)
dataList.append("np.dot ===> 多维矩阵相乘原始数据b")
dataList.append(sb)
dataList.append("np.dot(a,b) ===> 多维矩阵相乘后的值")
dataList.append(sc)
dataList.append("a.dot(b) ===> 多维矩阵相乘后的值")
dataList.append(sd)

# 2.5 随机数矩阵
ra = np.random.random((2,4))  # 前面一个random是生成0-1的随机数，后一个random是转换成2行4列的矩阵
dataList.append("np.random.random ===> 随机数矩阵")
dataList.append(ra)

# 2.6 对矩阵内元素进行运算
suma = np.sum(ra)   # 所有元素相加
sumb = np.sum(ra,axis=1)   # 如果axis = 1则以行为单位，下面的min,max都可以加axis参数
mina = np.min(ra)
maxa = np.max(ra)
dataList.append("np.sum ===> 所有元素相加")
dataList.append(suma)
dataList.append("np.sum ===> axis元素相加")
dataList.append(sumb)
dataList.append("np.min ===> 最小值")
dataList.append(mina)
dataList.append("np.max ===> 最大值")
dataList.append(maxa)

# 2.7 索引
tempa = np.arange(2,20).reshape((3,6))
indexa = np.argmax(tempa)  # 矩阵的最大索引
indexb = np.argmin(tempa)  # 矩阵的最小索引
dataList.append("np.reshape ===> 原始值")
dataList.append(tempa)  # 按行打印
dataList.append("np.tempa.T ===> 转置")
dataList.append(tempa.T)  # 按列打印
dataList.append("np.tempa.flat ===> 取每个元素")
dataList.append(tempa.flat)  # 打印每个元素
dataList.append("np.argmax ===> 矩阵的最大索引")
dataList.append(indexa)
dataList.append("np.argmin ===> 矩阵的最小索引")
dataList.append(indexb)

# 2.8 求矩阵的均值,下面两个函数的功能一样
avga = np.mean(tempa)
avgb = np.average(tempa)
dataList.append("np.mean ===> 矩阵的均值")
dataList.append(avga)
dataList.append("np.average ===> 矩阵的均值")
dataList.append(avgb)
avgc = tempa.mean()     # 求均值
dataList.append("tempa.mean() ===> 矩阵的均值")
dataList.append(avgc)
avgd = np.median(tempa)    # 求中位数
dataList.append("np.median ===> 矩阵的中位数")
dataList.append(avgd)

# 2.9 获取矩阵中的元素
la = tempa[2][3]
dataList.append("tempa[2][3] ===> 取矩阵的某个索引值")
dataList.append(la)

lb = tempa[1]
dataList.append("tempa[1] ===> 取矩阵的1维矩阵")
dataList.append(lb)

lc = tempa.flatten()    # 将矩阵转换为列表
dataList.append("tempa.flatten ===> 将矩阵转换为array")
dataList.append(lc)

# 2.10 获取每个元素的字节单位长度
itemsize = tempa.itemsize
dataList.append("tempa.itemsize ===> 每个元素的字节单位长度")
dataList.append(itemsize)

# 2.11 asarray函数，将List转换为ndarray
lx = [2,5,6,2,4,6]
ax = np.asarray(lx)
dataList.append("np.asarray ===> 将List转换为ndarray")
dataList.append(ax)

# 2.12 frombuffer函数，接受buffer输入转换为ndarray对象
stra = b'Husn ily caim ify'
bfa = np.frombuffer(stra,dtype="S1")   # numpy的bug，stra必须加b
dataList.append("np.frombuffer ===> 接受buffer输入转换为ndarray对象")
dataList.append(bfa)

# 2.13 fromiter将迭代对象回转成List对象
lista = range(5)
it = iter(lista)
fia = np.fromiter(it,dtype=float)
dataList.append("np.fromiter ===> 将迭代对象回转成list对象")
dataList.append(fia)

# 2.14 logspace:（对数）返回ndarray对象，其中包含在对数刻度上均匀分布的数字。刻度的开始和结束断点是某个地鼠的幂，通常为10
lpa = np.logspace(1.0,2.0,num=10)
dataList.append("np.logspace ===> 取对数log")
dataList.append(lpa)

# 2.15 切片和索引。类似python的切片。有三种可用的索引方法类型：字段访问，基本切片和高级索引。
# slice()函数
ara = np.arange(10)
sla = slice(2,7,2)
lla = ara[sla]
dataList.append("slice ===> 切片操作")
dataList.append(lla)

# 3.1 广播:如果两个数组的维数不相同，在Numpy中可以通过广播功能，实现对两个数组进行操作。

# 3.2 矩阵的迭代器
arb = np.arange(0,60,5)
arb = arb.reshape(3,4)
dataList.append("np.nditer ===> 迭代器，取每个元素")
dataList.append(np.nditer(arb))  # 迭代器，取每个元素

# 3.3 矩阵转置，即将m*n的矩阵转换成n*m的矩阵
arc = arb.T
dataList.append(".T ===> 矩阵转置前")
dataList.append(arb)
dataList.append(".T ===> 矩阵转置后")
dataList.append(arc)

# 3.4 C风格排序和F风格排序，C风格：迭代的时候按行顺序排序  F风格：迭代的时候按列风格排序
ard = arb.copy(order='C')
dataList.append("np.copy(order='C') ===> C风格迭代，按行")
dataList.append(np.nditer(ard))  # 按C风格迭代，也可以这样写np.nditer(arb,order='C)
are = arb.copy(order='F')
dataList.append("np.copy(order='F') ===> F风格迭代，按列")
dataList.append(np.nditer(are))   # 按F风格迭代，也可以这样写np.nditer(arb,order='F)

# 3.5 外部循环 ,flags标志，flags的参数包括：'c_index','f_index','multi_index','external_loop'
itera = np.nditer(arb,flags=['external_loop'],order='F')
dataList.append("np.nditer(,flags=['external_loop']) ===> 迭代器flag参数")
dataList.append(itera)

# 3.6 广播迭代，如果两个数组是可广播的，则nditer组合对象能够同时迭代它们。

# 3.7 ravel 将矩阵转换为一维数组，并按需返回。按行，按列，原顺序等
dataList.append("np.ravel ===> 将矩阵转换为一维数组")
dataList.append(arb.ravel(order='F'))

# 3.8 transpose 翻转给定数组的维度
trana = np.transpose(arb)
dataList.append("np.transpose ===> 翻转给定数组的维度")
dataList.append(trana)

# 3.9 vstack 对array进行合并。上下合并
vsa = np.array([1,1,1])
vsb = np.array([2,2,2])
vsc = np.vstack((vsa,vsb))
dataList.append("np.vstack ===> 对array进行合并。上下合并")
dataList.append(vsc)

# 3.10 hstack 左右合并
hsa = np.hstack((vsa,vsb))
dataList.append("np.hstack ===> 对array进行合并。左右合并")
dataList.append(hsa)

# 3.11 newaxis 转置函数，可以将m X n的矩阵转换成 n X m的矩阵
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
dataList.append("np.newaxis ===> 矩阵转置前原始数据A")
dataList.append(A)
dataList.append("np.newaxis ===> 矩阵转置前原始数据B")
dataList.append(B)

# 3.12 concatenate函数，合并多个矩阵。axis控制合并方向
# A B B A
# 1 2 2 1
# 1 2 2 1
# 1 2 2 1
cona = np.concatenate((A,B,B,A),axis=0)  # 按列合并
dataList.append("np.concatenate ===> 矩阵转置后按列合并")
dataList.append(cona)
conb = np.concatenate((A,B,B,A),axis=1)  # 按行合并
dataList.append("np.concatenate ===> 矩阵转置后按行合并")
dataList.append(conb)

# 3.13 矩阵的分割
# 等量分割
spa = np.arange(12).reshape((3,4))  # 创建一个3行4列的矩阵
dataList.append("np.split ===> 矩阵分割-等量分割原始数据")
dataList.append(spa)
spb = np.split(spa,2,axis=1)  # axis=1表示纵向分割，按2列分割
dataList.append("np.split ===> 矩阵等量分割-纵向分割")
dataList.append(spb)
spc = np.split(spa,3,axis=0)  # axis=0表示横向分割，按3行分割
dataList.append("np.split ===> 矩阵等量分割-横向分割")
dataList.append(spc)

# 不等量分割
spd = np.array_split(spa,3,axis=1)  # 按3列分割
dataList.append("np.split ===> 矩阵不等量分割-不等量分割原始数据")
dataList.append(spd)
spe = np.vsplit(spa,3)  # 横向分割，等同于np.split(spa,3,axis=0)
spf = np.hsplit(spa,2)  # 纵向分割，等同于np.split(spa,2,axis=1)
dataList.append("np.vsplit ===> 矩阵不等量分割-横向分割")
dataList.append(spe)
dataList.append("np.hsplit ===> 矩阵不等量分割-横向分割")
dataList.append(spf)

# 3.14 rollaxis 向后滚动到特定的轴，直到一个特定的位置。主要是指元素的坐标轴的交换
# 如：矩阵的第四个元素的坐标为ra[0,1,1]，轴2滚动到轴0后，坐标变为ra[1,0,1]
ra = np.arange(12).reshape(2,3,2)
dataList.append('np.rollaxis ===> 轴的滚动原始数据')
dataList.append(ra)
dataList.append('np.rollaxis ===> 轴的滚动,从轴2滚动到轴0')
dataList.append(np.rollaxis(ra,2))  # start默认为0
dataList.append('np.rollaxis ===> 轴的滚动,从轴0滚动到轴1')
dataList.append(np.rollaxis(ra,2,1))

# 3.15 swapaxes 交换数组的两个轴，主要是指元素的坐标轴的交换
# 如：矩阵的第二个元素的坐标为ra[0,0,1]，轴2和轴1交换后，坐标变为ra[1,0,0]
swa = np.swapaxes(ra,2,0)  # 轴2与轴0交换
dataList.append('np.swapaxes ===> 交换数组的两个轴')
dataList.append(swa)

# 3.16 广播broadcast
x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
b = np.broadcast(x,y)  # 返回的也是广播，类型为broadcast，可迭代对象
dataList.append('np.broadcast ===> 广播')
dataList.append('np.broadcast返回的类型:%s' % type(b))
dataList.append('np.broadcast返回的值:')
dataList.append(b)

# broadcast_to   将数组广播到新形状
ba = np.arange(4).reshape(1,4)
bb = np.broadcast_to(ba,(4,4)) # 将1 * 4的数组，变成4 * 4的矩阵
dataList.append('np.broadcast_to ===> 原始数据')
dataList.append(ba)
dataList.append('np.broadcast_to ===> 广播后的数据')
dataList.append(bb)

# 3.17 expand_dims 在指定位置插入新的轴来扩展数组形状
exa = np.arange(4).reshape(2,2)
exb = np.expand_dims(exa,axis=0)
exc = np.expand_dims(exa,axis=1)
dataList.append('np.expand_dims ===> 在指定位置插入新的轴，原始数据')
dataList.append(exa)
dataList.append('np.expand_dims ===> 在轴0插入新的轴后的数据')
dataList.append(exb)
dataList.append('np.expand_dims ===> 在轴1插入新的轴后的数据')
dataList.append(exc)

# 3.18 squeeze 从数组的形状中删除单一维度的条目,只有该维度里面只有一个元素的维度才可以删除。
sqa = np.arange(9).reshape(1,3,3)
dataList.append('np.squeeze ===> 从数组的形状中删除一维条目-原始数据')
dataList.append(sqa)
sqb = np.squeeze(sqa)
dataList.append('np.squeeze ===> 从数组的形状中删除一维条目-默认配置下删除后的数据')
dataList.append(sqb)
sqa = np.arange(9).reshape(3,1,3)
dataList.append('np.squeeze ===> 从数组的形状中删除一维条目-改变形状后的原始数据')
dataList.append(sqa)
sqc = np.squeeze(sqa,axis=1)
dataList.append('np.squeeze ===> 从数组的形状中删除一维条目-axis=1删除后的数据')
dataList.append(sqc)

# 3.19 resize 改变原矩阵的形状，如果新矩阵的大小大于原矩阵的大小，则新矩阵包含原矩阵的元素
rea = np.arange(6).reshape(2,3)
dataList.append('np.resize ===> 改变矩阵的形状-原始数据')
dataList.append(rea)
reb = np.resize(rea,(3,2))
dataList.append('np.resize ===> 改变矩阵的形状后数据')
dataList.append(reb)
reb = np.resize(rea,(3,3))
dataList.append('np.resize ===> 改变矩阵的形状后数据')
dataList.append(reb)

# 3.20 append 在数组的后面插入值
apa = np.arange(6).reshape(2,3)
dataList.append('np.append ===> 在矩阵末尾添加新的值-原始数据')
dataList.append(apa)
apb = np.append(apa,[6,7,8])
dataList.append('np.append ===> 在矩阵末尾添加新的值后的数据')
dataList.append(apb)
apb = np.append(apa,[[7,8,9]],axis=0)
dataList.append('np.append ===> 在矩阵末尾沿轴0添加新的值后的数据')
dataList.append(apb)
apb = np.append(apa,[[10,8],[2,1]],axis=1)
dataList.append('np.append ===> 在矩阵末尾沿轴1添加新的值后的数据')
dataList.append(apb)

# 3.21 tile  对矩阵进行扩展
tia = np.array([0,1,2])   # 一维数组  1 * 3
dataList.append('np.tile ===> 对一维矩阵进行复制扩展-原始数据')
dataList.append(tia)
dataList.append('np.tile(a,2) ===> 对一维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tia,2))
dataList.append('np.tile(a,(2,1)) ===> 对一维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tia,(2,1)))
dataList.append('np.tile(a,(2,2)) ===> 对一维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tia,(2,2)))
dataList.append('np.tile(a,(2,1,2)) ===> 对一维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tia,(2,1,2)))

tib = np.array([[1,2],[3,4]])
dataList.append('np.tile ===> 对二维矩阵进行复制扩展-原始数据')
dataList.append(tib)
dataList.append('np.tile(a,2) ===> 对二维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tib,2))
dataList.append('np.tile(a,(2,1)) ===> 对二维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tib,(2,1)))
dataList.append('np.tile(a,(2,2)) ===> 对二维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tib,(2,2)))
dataList.append('np.tile(a,(2,1,2)) ===> 对二维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tib,(2,1,2)))
dataList.append('np.tile(a,(2,2,1,2)) ===> 对二维矩阵进行复制扩展后的数据')
dataList.append(np.tile(tib,(2,2,1,2)))

# 3.22 insert 沿给定的轴在输入数组中插入值
ina = np.arange(6).reshape(3,2)
dataList.append('np.insert ===> 沿给定的轴在输入数组中插入值-原始数据')
dataList.append(ina)
dataList.append('np.insert(ina,3,[11,22]) ===> 沿给定的轴在输入数组中插入值未传递axis参数情况后的数据')
dataList.append(np.insert(ina,3,[11,22]))
dataList.append('np.insert(ina,1,[11],axis=0) ===> 沿给定的轴在输入数组中插入值axis=0')
dataList.append(np.insert(ina,1,[11],axis=0))
dataList.append('np.insert(ina,1,11,axis=1) ===> 沿给定的轴在输入数组中插入值axis=1')
dataList.append(np.insert(ina,1,11,axis=1))

# 3.23 unique 去重，将重复元素去掉。
dataList.append('np.unique ===> 去重,原始数据')
ua = np.array([5,2,6,2,4,3,6,2,4,7,8,2])
dataList.append(ua)
dataList.append('np.unique(ua) ===> 去重，返回结果，并按从小到大的顺序排序')
dataList.append(np.unique(ua))
dataList.append('np.unique(ua,return_index=True) ===> 去重，返回输入数组中的元素下标')
dataList.append(np.unique(ua,return_index=True))
dataList.append('np.unique(ua,return_inverse=True) ===> 去重，返回原数组中的元素在去重数组中的下标，可以重构原数组')
ub,index = np.unique(ua,return_inverse=True)
dataList.append(ub)
dataList.append('np.unique(ua,return_inverse=True) ===> 去重，返回去重数组中的元素下标，重构原数组---ub[index]')
dataList.append(ub[index])
dataList.append('np.unique(ua,return_counts=True) ===> 去重，返回去重数组中的元素在原始数组中的出现的次数')
dataList.append(np.unique(ua,return_counts=True))

# 4 位运算
# 4.1 bitwise_and 按位与
bita,bitb = 13,17
bitaa,bitbb = bin(13),bin(17)  # 将数字转换成二进制
dataList.append('bitwise ===> 位运算，原始数据')
dataList.append(bitaa+" "+bitbb)
dataList.append('bitwise_and ===> 按位与')
dataList.append(np.bitwise_and(bita,bitb))

# 4.2 bitwise_or 按位或
dataList.append('bitwise_or ===> 按位或')
dataList.append(np.bitwise_or(bita,bitb))

# 4.3 invert 按位非
dataList.append('invert ===> 13的按位非')
ina = np.invert(np.array([13],dtype=np.uint8))   # 返回的是一个数组
dataList.append(ina)
dataList.append('invert ===> 13的二进制表示')
dataList.append(np.binary_repr(13,width=8))
dataList.append('invert ===> 13按位非的二进制表示')
dataList.append(np.binary_repr(ina[0],width=8))  # 这里取这个数组的第一个元素，因为这个数组只有一个元素

# 4.4 left_shift 位左移，right_shift 位右移，用法相同
dataList.append('np.left_shift(10,2) ===> 位左移，将10左移两位')
lsa = np.left_shift(10,2)
dataList.append(lsa)
dataList.append('np.left_shift(10,2) ===> 位左移，10的二进制表示')
dataList.append(np.binary_repr(10,width=8))
dataList.append('np.left_shift(10,2) ===> 位左移，10左移2位后的二进制表示')
dataList.append(np.binary_repr(lsa,width=8))

# 5 舍入函数
# 5.1 around 四舍五入，decimals参数：要舍入的小数位数。默认为0.如果为负，整数将四舍五入到小数点左侧的位置
ara = np.array([1.0,5.55,123,0.567,25.532])
dataList.append('np.around ===> 四舍五入 原始值')
dataList.append(ara)
dataList.append('np.around(ara) ===> decimals参数缺省')
dataList.append(np.around(ara))
dataList.append('np.around(ara,decimals = 1) ===> 四舍五入')
dataList.append(np.around(ara,decimals=1))
dataList.append('np.around(ara,decimals = -1) ===> 为负值，则四舍五入整数')
dataList.append(np.around(ara,decimals=-1))

# 5.2 floor 返回不大于输入参数的最大整数
fla = np.array([-1.7,1.5,-0.2,0.6,10])
dataList.append('np.floor ===> 返回不大于输入参数的最大整数 原始值')
dataList.append(fla)
dataList.append('np.floor ===> 舍入后的值')
dataList.append(np.floor(fla))

# 5.3 ceil 返回输入值的上限
dataList.append('np.ceil ===> 舍入后的值')
dataList.append(np.ceil(fla))

# 6 算术运算
# 6.1 加减乘除 add(),subtract(),multiply(),divide(),乘方：power,整除取余：mod()
# 6.2 高等数学
# 6.2.1 reciprocal 倒数
rea = np.array([0.25,1.33,1,100])
dataList.append('np.reciprocal ===> 倒数，原始数据')
dataList.append(rea)
dataList.append('np.reciprocal ===> 倒数值')
dataList.append(np.reciprocal(rea))

# 6.2.2 ptp,返回沿轴的最大值-最小值
pta = np.array([[3,6,1],[4,8,2],[9,0,3]])
dataList.append('np.ptp ===> 返回沿轴的最大值-最小值,原始值')
dataList.append(pta)
dataList.append('np.ptp ===> axis缺省情况,最大原始-最小原始')
dataList.append(np.ptp(pta))
dataList.append('np.ptp(pta,axis=1) ===> 返回沿轴的最大值-最小值')
dataList.append(np.ptp(pta,axis=1))
dataList.append('np.ptp(pta,axis=0) ===> 返回沿轴的最大值-最小值')
dataList.append(np.ptp(pta,axis=0))

# 6.2.3 百分位数 percentile
pera = np.array([[30,40,70],[80,20,10],[50,90,60]])
dataList.append('np.percentile ===> 百分位数 原始值')
dataList.append(pera)
dataList.append('np.percentile(pera,50) ===> 百分位数 axis缺省')
dataList.append(np.percentile(pera,50))
dataList.append('np.percentile(pera,50，axis=1) ===> 百分位数 axis=1')
dataList.append(np.percentile(pera,50,axis=1))
dataList.append('np.percentile(pera,50，axis=0) ===> 百分位数 axis=0')
dataList.append(np.percentile(pera,50,axis=0))

# 6.2.4 中位数 median   算术平均值mean  加权平均值average
# 6.2.5 标准差公式：sqrt(mean((x - x.mean())**2))
# 方差公式：标准差是方差的平方根

# 7、排序，搜索
# 7.1 sort 排序 如果axis参数缺省，则将矩阵展开
soa = np.array([[3,7],[9,1],[3,6]])
dataList.append('np.sort ===> 排序，原始数据')
dataList.append(soa)
dataList.append('np.sort ===> 排序，axis缺省')
dataList.append(np.sort(soa))
dataList.append('np.sort(soa,axis=0) ===> 排序，axis=0')
dataList.append(np.sort(soa,axis=0))
dt = np.dtype([('name','S10'),('age',int)])
sob = np.array([('husn',32),('caim',25),('luyh',26),('huyy',30),('weiy',30)],dtype=dt)
dataList.append('np.sort ===> 名字，原始数据')
dataList.append(sob)
dataList.append('np.sort(sob,order=\'name\') ===> 按名字排序')
dataList.append(np.sort(sob,order='name'))

# 7.2 argsort 沿给定轴间接排序，并使用指定排序类型返回数据的函数索引
arga = np.array([2,1,3])
dataList.append('np.argsort ===> 间接排序 原始数据')
dataList.append(arga)
dataList.append('np.argsort(arga) ===> 间接排序')
dataList.append(np.argsort(arga))

# 8、字符串函数，numpy中的字符串操作主要是针对数组的
# 8.1 add() 返回两个str或unicode数组的逐个字符串连接
dataList.append('char.add ===> 数组字符串操作原始数据')
stra = np.array(['hsn'])
strb = np.array(['ily'])
dataList.append('%s \n %s' % (stra,strb))
dataList.append('char.add ===> 数组字符串操作拼接后的数据')
dataList.append(np.char.add(stra,strb))
dataList.append('char.add ===> 多维数组字符串操作原始数据')
stra = np.array(['hsn','caim','sjj'])
strb = np.array(['ily','ify','icy'])
dataList.append('%s \n %s' % (stra,strb))
dataList.append('char.add ===> 多维数组字符串操作拼接后的数据')
dataList.append(np.char.add(stra,strb))

# 8.2 char.multiply()多重连接
cma = np.array(['hsnify'])
dataList.append('char.multiply ===> 多重连接原始数据')
dataList.append(cma)
dataList.append('char.multiply ===> 多重连接3次后的数据')
dataList.append(np.char.multiply(cma,3))

# 8.3 char.center() 按格式返回数组，即以当前字符串为中心，根据格式宽度进行填充
ccena = np.array(['caim ifcy'])
dataList.append('char.center ===> 以字符串为中心左右岸要求进行填充=原始数据')
dataList.append(ccena)
dataList.append('char.center ===> 以字符串为中心左右岸要求进行填充=返回数据')
dataList.append(np.char.center(ccena,20,fillchar='*'))

# 8.4 char.capitalize() 第一个字符转换为大写，char.title() 每一个单词的首字母大写
# char.lower() 所有字符转换为小写。upper所有字符全转换为大写。split()字符串分割，默认按空格分割
# splitlines() 以换行符进行分割。
cspa = np.array(['hsn ily ity imy iqy ify icy iby icy'])
dataList.append('char.split ===> 字符串分割=原始数据')
dataList.append(cspa)
dataList.append('char.split ===> 字符串分割=返回数据')
dataList.append(np.char.split(cspa))
dataList.append('char.split ===> 多维字符串分割=原始数据')
cspa = np.array(['hsn,ily','caim,ify'])
dataList.append(cspa)
dataList.append('char.split ===> 多维字符串分割=返回数据')
dataList.append(np.char.split(cspa,sep=','))

# 8.5 strip() 去掉字符串前后指定的特定字符
csta = np.array(['ahsn ilya','acaim ify','sunjj icya'])
dataList.append('char.strip ===> 去掉前后的指定字符=原始数据')
dataList.append(csta)
dataList.append('char.strip ===> 去掉前后的指定字符=返回数据')
dataList.append(np.char.strip(csta,'a'))

# 8.6 char.join返回一个字符串，其中单个字符由指定的分隔符连接
cja = np.array(['hsn'])
dataList.append('char.join ===> 在各个字符之间插入指定字符=原始数据')
dataList.append(cja)
dataList.append('char.join ===> 在各个字符之间插入指定字符=返回数据')
dataList.append(np.char.join(':',cja))
cja = np.array(['hsn','ily'])
dataList.append('char.join ===> 多维数组在各个字符之间插入指定字符=原始数据')
dataList.append(cja)
dataList.append('char.join ===> 多维数组在各个字符之间插入指定字符=返回数据')
dataList.append(np.char.join([':','-'],cja))

# 测试函数
def testNumpy():

    copyTest()

    if len(dataList):
        for data in dataList:
            if isinstance(data,str):  # 如果是字符串，则直接打印
                print(data)
            else:
                # 判断对象是迭代对象，但不是多维数组
                if isinstance(data, Iterable) and not isinstance(data, np.ndarray):
                    util.printIterData(data)
                else:
                    util.printData(data)
    else:
        print("data list is null")


def copyTest():
    # 如：一个数组的维度为3X4,另一个数组的维度为1X4,则：
    arrayb = np.array([1, 2, 3, 4], dtype=int)
    iterb = np.nditer([arb, arrayb])  # 同时迭代两个数组
    print('np.nditer ===> 同时迭代两个数组')
    for x, y in iterb:
        print('%d:%d' % (x, y))
    util.printLine()

    print('.ndim ===> 矩阵的维度')
    util.printData('number of dim:%s' % arangeb.ndim)  # 维度
    print('.shape ===> 矩阵的形状行数，列数')
    print('shape :', arangeb.shape)  # 行数和列数
    print('.size ===> 矩阵的元素个数')
    util.printData('size:%s' % arangeb.size)  # 元素个数
    # 3.14 浅拷贝和深拷贝
    # =赋值带有关联性
    a = np.arange(4)  # [0,1,2,3]
    b = a
    c = a
    d = b
    # 以上改变a的值，b,c,d都会跟着改变，改变d的值，a,b,c也会都跟着变。
    a[0] = 11
    print('b=a ===> =赋值带有关联性')
    print('b is a: %s' % (b is a))
    print('c is a: %s' % (c is a))
    print('d is a: %s' % (d is a))
    d[1:3] = [22, 33]  # 将d的第2,3个元素修改
    print('a:%s' % a)
    print('b:%s' % b)
    print('c:%s' % c)
    print('d:%s' % d)
    # copy()赋值没有关联性
    b = a.copy()
    print('copy() ===> copy()赋值没有关联性')
    print('b copy a:%s' % b)
    a[3] = 44
    print('a update:%s' % a)
    util.printData('b value:%s' % b)


if __name__ == "__main__":
    testNumpy()

