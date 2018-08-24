#! /Users/michael/anaconda3/bin/python
# @Date:   2018-08-24 15:24:52

def my_int(s):
    numbers = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }

    total = 0
    for i,n in enumerate(reversed(s)):
        total += numbers[n]*10**i

    return total

print(my_int('123'))