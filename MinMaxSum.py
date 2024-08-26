#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sums = []
    for i, _ in enumerate(arr):
        a = arr.copy()
        a.pop(i)
        sums.append(sum(a))
    s_sums = sorted(sums)
    print(min(s_sums), max(s_sums))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
