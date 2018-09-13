#! /Users/michael/anaconda3/bin/python
# @Date:   2018-09-13 12:37:13

"""
题目：已知一个能产生 1-9 随机数的函数 nine，求一个能产生 1-10 随机数的函数 ten。

思路简单：
随机两次，产生 9x9 = 81 中组合。当为最后一种组合时，舍弃重来。
确保产生 11 ~ 98 一共 80中组合，注意是 80 种组合，不是 98-11+1=88 种，因为不含 0。
你可以看出，这些组合虽然总的概率不为1，但是每个组合的概率均等。
于是我可以分成 10 组，得到的结果在哪一行，那么行号就是那个我要的随机数。

如何确定每个组合的边界？

可以用把这 80 个数放入矩阵：
def matrix():
    for i in range(1, 10):
        for j in range(1, 10):
            nums.append(i*10+j)
    nums.pop()
    arr = np.array(nums).reshape(10, 8)
    print(arr)

[[11 12 13 14 15 16 17 18]
 [19 21 22 23 24 25 26 27]
 [28 29 31 32 33 34 35 36]
 [37 38 39 41 42 43 44 45]
 [46 47 48 49 51 52 53 54]
 [55 56 57 58 59 61 62 63]
 [64 65 66 67 68 69 71 72]
 [73 74 75 76 77 78 79 81]
 [82 83 84 85 86 87 88 89]
 [91 92 93 94 95 96 97 98]]
"""

import random
import numpy as np

def nine():
    return random.randint(1,9)


def ten():
    while True:
        first = nine()
        second = nine()
        if first == 9 and second == 9:
            continue
        else:
            break
    tmp = first*10 + second
    if 11 <= tmp <= 18:
        return 1
    elif 19 <= tmp <= 27:
        return 2
    elif 28 <= tmp <= 36:
        return 3
    elif 37 <= tmp <= 45:
        return 4
    elif 46 <= tmp <= 54:
        return 5
    elif 55 <= tmp <= 63:
        return 6
    elif 64 <= tmp <= 72:
        return 7
    elif 73 <= tmp <= 81:
        return 8
    elif 82 <= tmp <= 89:
        return 9
    elif 91 <= tmp <= 98:
        return 10


num_dict = {}
for i in range(100000):
    n = ten()
    if n not in num_dict:
        num_dict[n] = 1
    else:
        num_dict[n] += 1

print(num_dict)

