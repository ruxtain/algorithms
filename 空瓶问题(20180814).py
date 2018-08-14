#! /Users/michael/anaconda3/bin/python
# @Date:   2018-08-14 19:40:57

"""

3 个空瓶可以换 1 瓶水，n 个空瓶能换多少？

例如：10个空瓶，可以换 3 瓶并剩余 1 个空瓶，喝完后得到 4 个空瓶，（喝了3瓶）
然后又换一瓶，得到 2 个空瓶 （又喝了一瓶），2 个空瓶可以直接赊账拿一瓶，喝完后推给老板 3 个空瓶。
一共 5 瓶。
water(10) 应当等于 5。

"""

def water(n):
    total = 0
    while True:
        ret = n//3 # 第一轮能换的水数
        left = n%3 # 第一轮不足以凑够 3 个空瓶而剩下的空瓶
        if ret == 0:
            if left == 2: # 即使凑不够，最终能剩 2 个空瓶，就能再赊账换一瓶水
                total += 1
            break
        total += ret
        n = ret + left # 喝光刚换的水，新一轮的空瓶数

    return total

for i in range(1, 16):
    print(i, water(i))


