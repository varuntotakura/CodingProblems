#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    sp = s.split(":")
    end_sp = sp[-1][-2:]
    sp[-1] = sp[-1][:2]
    if end_sp == "AM":
        if sp[0] == "12":
            sp[0] = "00"
    elif end_sp == "PM":
        if sp[0] != "12":
            in_str = int(sp[0])
            sp[0] = str(12+in_str)
    return ":".join(sp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
