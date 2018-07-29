#! /Users/michael/anaconda3/bin/python
# @Author: ruxtain
# @Date:   2018-07-29 20:15:39

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            ret = int(str(x)[::-1])
            return 0 if ret > 2147483647 else ret
        else:
            ret = 0 - int(str(x)[:0:-1])
            return 0 if ret < -2147483648 else ret

