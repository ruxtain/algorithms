#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: ruxtain
# @Date:   2018-07-19 11:38:39
# @Last Modified by:   ruxtain
# @Last Modified time: 2018-07-19 15:06:24

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

1
1 1
1 1+1 1

"""

def fun(numRows):

    '''
    得到第 numRows 为止的整个杨辉三角
    追求性能，刻意不使用递归
    '''

    def nextRow(currentRow):
        result = []
        for i in range(len(currentRow)-1):
            result.append(currentRow[i] + currentRow[i+1])
        return [1] + result + [1]

    root = []
    for i in range(numRows):
        if i == 0:
            root.append([1])
        else:
            root.append(nextRow(root[-1]))
    return root


import math
def fun2(numRows):

    '''
    得到杨辉三角的第 numRows 行
    要求：
    你可以优化你的算法到 O(k) 空间复杂度吗？

    c(6, 0)=1
    c(6, 1)=6 / 1!
    c(6, 2)=6 x 5 / 2!
    c(6, 3)=6 x 5 x 4 / 3!
    ...
    c(6, 6)=6 x 5 x 4 x 3 x 2 x 1 / 6! = 1
    '''
    def numerator(n, times):
        result = 1
        while times > 0:
            result = result * n
            n -= 1
            times -= 1
        return result

    def c(n, m):
        '''
        高中数学的组合数
        我不 import math 写个阶乘也很简单，不过算了，没必要..
        '''
        nu = numerator(n, m)
        fa = math.factorial(m)
        return int(nu/fa)

    result = []
    for i in range(numRows+1):
        result.append(c(numRows, i))
    return result

if __name__ == '__main__':
    print(fun(6))
    print(fun2(3))












