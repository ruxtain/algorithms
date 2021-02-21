#!/Users/michael/anaconda3/bin/python

import math, sys

def my_sqrt(x, precision=2):

    if x < 0:
        return None

    def get_root(x, root, step):
        i = -step
        while True:
            i += step
            if (x - (root + i) ** 2 > 0 and x - (root + i + step) ** 2 < 0)  or (x - (root + i) ** 2 == 0):
                return root + i

    root = 0
    for p in range(precision + 2): # 多算一位，再来 round 回来
        step = 10 ** (-p)
        # print('step =', step)
        # print('x =', x)
        root = get_root(x, root, step)
    return round(root, precision)


# for testing:
for x in [0.4356, 0.1, -1, 100, 1000]:
    for p in range(1, 5): 
        print("my_sqrt({}, {}) = {}".format(x, p, my_sqrt(x, precision=p)))
