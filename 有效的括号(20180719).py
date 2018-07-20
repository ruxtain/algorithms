#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: ruxtain
# @Date:   2018-07-19 09:58:47
# @Last Modified by:   ruxtain
# @Last Modified time: 2018-07-19 11:18:40
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

'''
思想：

只需要一次遍历外加一个空的列表q
一旦发现左括号就加入q，
一旦发现右括号就和q最后一项比较看是否匹配，匹配则去掉这最后一项，不匹配则直接返回 False
如果都匹配成功，则最终必须返回一个空的q
'''

def fun(s):
        d = {'(':')','{':'}','[':']'}
        if s == '':
            return True # 可以是空字符

        if s[0] not in d:
            return False

        q =[]
        for i in s:
            if i not in d: # 不在 d 键，那么必须是括闭
                if len(q) > 0 and d[q.pop()] == i : # 发现一对
                    continue
                else:
                    return False
            elif i in d:
                q.append(i)
        return not q # q 必须为空

if __name__ == '__main__':
    
    for i in ['[{()}]()', '([])', '([})', '{{}}[(}})]', '', '}{', '[', '((', ')']:
        print(i, fun(i))
        print('-----------------')





































