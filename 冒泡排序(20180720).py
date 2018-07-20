#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: ruxtain
# @Date:   2018-07-20 17:30:08
# @Last Modified by:   ruxtain
# @Last Modified time: 2018-07-20 17:48:44

def bubble_sort(nums):
    length = len(nums)
    while length > 0:
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        length-=1
    return nums

if __name__ == '__main__':
    nums = [9, 2, 1, 3, 9, 8, 7, 6, 5, 0, 12, 3]
    print(bubble_sort(nums))