#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr = sorted(arr)
    total = len(arr)
    minus = 0
    plus = 0
    zero = 0
    for i in arr:
        if i < 0:
            minus += 1
        elif i == 0:
            zero += 1
        elif i > 0:
            plus += 1
    print("{:0.6f}".format(plus/total))
    print("{:0.6f}".format(minus/total))
    print("{:0.6f}".format(zero/total))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
