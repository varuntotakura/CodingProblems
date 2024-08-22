# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix) // 2
    total_sum = 0
    
    for i in range(n):
        for j in range(n):
            # We consider the four possible positions:
            top_left = matrix[i][j]
            top_right = matrix[i][2*n - j - 1]
            bottom_left = matrix[2*n - i - 1][j]
            bottom_right = matrix[2*n - i - 1][2*n - j - 1]
            
            # Add the maximum of the four to the sum
            total_sum += max(top_left, top_right, bottom_left, bottom_right)
    
    return total_sum

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        
        result = flippingMatrix(matrix)
        print(str(result))


# 1
# 2
# 112 42 83 119
# 56 125 56 49
# 15 78 101 43
# 62 98 114 108