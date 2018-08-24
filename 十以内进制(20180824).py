#! /Users/michael/anaconda3/bin/python
# @Date:   2018-08-24 15:23:52

a = "1"
b = "8"

# 可以是10进制以下的任意进制
system = 9 

def to_ten(n):
    # 转成10进制
    n = n[::-1]
    total = 0
    for i in range(len(n)):
        total += int(n[i])*(system**i)
    return total

def to_system(n):
    # 转回原来的进制
    R = []
    while n >= system:
        r = n % system
        n = n // system
        R.append(str(r))
    R.append(str(n))
    return ''.join(R[::-1])

def add(a, b):
    # 相加
    ten = to_ten(a) + to_ten(b)
    return to_system(ten)

print(add(a,b))

