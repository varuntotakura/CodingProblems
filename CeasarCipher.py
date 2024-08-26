#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = []
    for o in s:
        if 'a' <= o <= 'z':  # Lowercase letters
            c = ord(o) - ord('a')
            r = (c + k) % 26
            res = chr(r + ord('a'))
        elif 'A' <= o <= 'Z':  # Uppercase letters
            c = ord(o) - ord('A')
            r = (c + k) % 26
            res = chr(r + ord('A'))
        else:  # Non-alphabetic characters
            res = o
        result.append(res)
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
