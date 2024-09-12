#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getFinalImage' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY image
#  2. INTEGER rotation
#  3. INTEGER vertical_flip
#  4. INTEGER horizontal_flip
#

import numpy as np

class BinaryMatrixProcessor:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate_90(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        rotated = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - i - 1] = self.matrix[i][j]
        return rotated

    def rotate_180(self):
        return [row[::-1] for row in self.matrix[::-1]]

    def rotate_270(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        rotated = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated[cols - j - 1][i] = self.matrix[i][j]
        return rotated

    def flip_vertical(self):
        return self.matrix[::-1]

    def flip_horizontal(self):
        return [row[::-1] for row in self.matrix]

def getFinalImage(image, rotation, vertical_flip, horizontal_flip):
    # Write your code here
    processor = BinaryMatrixProcessor(image)
    if rotation == 90:
        matrix = processor.rotate_90()
    elif rotation == 180:
        matrix = processor.rotate_180()
    elif rotation == 270:
        matrix = processor.rotate_270()
    if vertical_flip:
        matrix = np.flipud(matrix)
    if horizontal_flip:
        matrix = np.fliplr(matrix)
    return matrix
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    image_rows = int(input().strip())
    image_columns = int(input().strip())

    image = []

    for _ in range(image_rows):
        image.append(list(map(int, input().rstrip().split())))

    rotation = int(input().strip())

    vertical_flip = int(input().strip())

    horizontal_flip = int(input().strip())

    result = getFinalImage(image, rotation, vertical_flip, horizontal_flip)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
