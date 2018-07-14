#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: Michael Tan
# @Date:   2018-07-14 15:37:40
# @Last Modified by:   Michael Tan
# @Last Modified time: 2018-07-14 16:21:51

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
'''

def get_digit(n):
    '''判断 n 有多少位数'''
    i = 1
    while True:
        if n - 10 ** i < 0:
            return i
        else:
            i += 1

def get_num_list(n):
    '''
    映射数字n每一位的数字到一个列表
    顺序和原数字一样
    '''
    num_list = []
    digit = get_digit(n)
    for i in range(digit, 0, -1):
        d = n // 10 ** (i-1)
        num_list.append(d)
        n = n - d * 10 ** (i-1)
    return num_list

def is_palindrome(n):
    '''
    正反两边同时进行取值并比较，不管数位是奇数还是偶数，是没有影响的
    注意负数一律不对称
    '''
    if n >= 0:
        num_list = get_num_list(n)
        digit = get_digit(n)
        return all(num_list[i] == num_list[-(i+1)] for i in range(int(digit/2)))
    else:
        return False


if __name__ == '__main__':
    for i in [121, 11, 1, 100, 213, 78787878787878787, 666, -121]:
        print('{} is a palindrome? {}'.format(i, is_palindrome(i)))












