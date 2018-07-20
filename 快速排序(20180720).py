#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: ruxtain
# @Date:   2018-07-20 17:59:41
# @Last Modified by:   ruxtain
# @Last Modified time: 2018-07-20 18:03:19

def quick_sort(nums):
    out = []
    big = []
    sml = []
    if not nums:
        return nums
    current = nums.pop()
    for i in nums:
        if i > current:
            big.append(i)
        else:
            sml.append(i)
    return quick_sort(sml) + [current] + quick_sort(big) 


if __name__ == '__main__':
    nums = [9, 2, 1, 3, 9, 8, 7, 6, 5, 0, 12, 3]
    print(quick_sort(nums))