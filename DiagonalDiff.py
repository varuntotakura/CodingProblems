#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_right_diagonal = 0
    right_left_diagonal = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                left_right_diagonal += arr[i][j]
    l = range(len(arr))
    for i, j in list(zip(l, l[::-1])):
        right_left_diagonal += arr[i][j]
    return abs(left_right_diagonal - right_left_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
