def is_border(i, j, matrix):
    if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1:
        return True
    return False

def is_outside(i, j, matrix):
    if i < 0 or i > len(matrix)-1 or j < 0 or j > len(matrix[0])-1:
        return True
    return False

def check_around(i, j, matrix, border_islands):
    steps = {(0, 1), (1, 0), (0, -1), (-1, 0)}
    for (ix, jx) in steps:
        new_i = i + ix
        new_j = j + jx
        if is_border(new_i, new_j, matrix) and not is_outside(new_i, new_j, matrix):
            border_islands[new_i, new_j] = True
            check_around(new_i, new_j, matrix, border_islands)
    return border_islands

def removeIslands(matrix):
    border_islands = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if is_border(i, j, matrix):
                border_islands[i, j] = True
                border_islands = check_around(i, j, matrix, border_islands)
    return matrix