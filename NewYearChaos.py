#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # bribes = 0
    # d = {}
    # for i in set(q):
    #     d[i] = 0
    # i = 0
    # while i < len(q)-1:
    #     if q[i] <= q[i+1]:
    #         i += 1
    #     else:
    #         temp = q[i]
    #         q[i] = q[i+1]
    #         q[i+1] = temp
    #         d[q[i+1]] += 1
    #         bribes += 1
    #         i = 0
    # if sorted(d.values())[-1] >= 3:
    #     print("Too chaotic")
    # else:
    #     print(bribes)
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
