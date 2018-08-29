#! /Users/michael/anaconda3/bin/python
# @Date:   2018-08-29 16:09:52

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

输入: "afhabefkjojkfsfdfsdjn"
输出: "fkjojkf"

"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        longest_target = ''

        if all([i==s[0] for i in s]):
            return s

        for i in range(n):
            target = [s[i]]
            count = 1
            while True:
                if i + count < n and i - count >= 0:
                    prev_one = s[i-count]
                    next_one = s[i+count]
                    count += 1
                else:
                    break

                if prev_one == next_one:
                    target.insert(0, prev_one)
                    target.append(next_one)
                elif s[i] in [prev_one, next_one] and len(target) == 1:
                    target.append(s[i])
                    break
                else:
                    break

            if len(target) > len(longest_target):
                longest_target = ''.join(target)

        for i in range(n):
            if i+1 < n and s[i] == s[i+1]:
                target = [s[i], s[i+1]]
                count = 1
            else:
                continue
            while True:
                if i + count + 1 < n and i - count >= 0:
                    prev_one = s[i-count]
                    next_one = s[i+count+1]
                    count += 1
                else:
                    break

                if prev_one == next_one:
                    target.insert(0, prev_one)
                    target.append(next_one)
                else:
                    break

            if len(target) > len(longest_target):
                longest_target = ''.join(target)

        return longest_target

print(Solution().longestPalindrome(""))




