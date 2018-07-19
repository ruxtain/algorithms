#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: Michael Tan
# @Date:   2018-07-14 16:45:43
# @Last Modified by:   Michael Tan
# @Last Modified time: 2018-07-14 16:57:24

'''
https://leetcode-cn.com/problems/single-number/description/

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''


nums = [2, 2, 1, 3, 3]
nums = [4,1,2,1,2]
nums = [1,1,2,2,4]
nums = [1,1,3,2,2]

def get(nums):
    nums.sort()
    for i in range(0, len(nums)-1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    else:
        return nums[-1]

print(get(nums))


    