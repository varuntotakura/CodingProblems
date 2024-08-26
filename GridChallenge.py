#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    tgrid = []
    if len(grid)==1:
        return "YES"
    for aset in grid:
        row = []
        for c in aset:
            row.append(c)
        tgrid.append(sorted(row))
    t_tgrid = [[tgrid[j][i] for j in range(len(tgrid))] for i in range(len(tgrid[0]))]
    print(t_tgrid, "\n", sorted(t_tgrid))
    st_tgrid = t_tgrid.copy()
    for i, aset in enumerate(t_tgrid):
        st_tgrid[i] = sorted(aset)
    if t_tgrid == st_tgrid:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
