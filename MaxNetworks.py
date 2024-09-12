#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximumNetworks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY speed
#  2. INTEGER minComps
#  3. LONG_INTEGER speedThreshold
#

def maximumNetworks(speed, minComps, speedThreshold):
    # Write your code here
    n = len(speed)
    total_networks = 0
    i = 0
    while i <= n - minComps:
        for j in range(i + minComps, n + 1):
            network_speed = sum(speed[i:j])
            if network_speed >= speedThreshold:
                total_networks += 1
                i = j
                break
        else:
            i += 1
    return total_networks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    speed_count = int(input().strip())

    speed = []

    for _ in range(speed_count):
        speed_item = int(input().strip())
        speed.append(speed_item)

    minComps = int(input().strip())

    speedThreshold = int(input().strip())

    result = maximumNetworks(speed, minComps, speedThreshold)

    fptr.write(str(result) + '\n')

    fptr.close()
