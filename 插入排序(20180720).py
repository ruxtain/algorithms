#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: ruxtain
# @Date:   2018-07-20 19:18:16
# @Last Modified by:   ruxtain
# @Last Modified time: 2018-07-20 19:39:21

def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        # “冻结”当前这项，抽离出来
        temp = nums[i]
        j = i
        # 如果当前项比前面的项小，则继续往前比较
        # 并把当前项前面这项复制到后面的位置，占掉刚刚当前项的位置
        # 以此类推，直到 j >= 1，即 j-1>=0，比到了最前面
        while temp < nums[j-1] and j >= 1:
            nums[j]  = nums[j-1]
            j -= 1
        # 把抽离出来的那一项放回
        nums[j] = temp 
    return nums


    

if __name__ == '__main__':
    nums = [9, 2, 1, 3, 9, 8, 7, 6, 5, 0, 12, 3]
    print(insert_sort(nums))    