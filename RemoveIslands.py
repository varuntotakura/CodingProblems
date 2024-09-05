def is_border(i, j, matrix):
    if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1:
        return True
    return False

def is_outside(i, j, matrix):
    if i < 0 or i > len(matrix)-1 or j < 0 or j > len(matrix[0])-1:
        return True
    return False

def make_key(i, j):
    return f"{i}{j}"

def check_around(i, j, matrix, border_islands):
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for (ix, jx) in steps:
        new_i = i + ix
        new_j = j + jx
        if is_outside(new_i, new_j, matrix):
            continue
        neigh = matrix[new_i][new_j]
        key = make_key(new_i, new_j)
        if neigh == 1 and not key in border_islands:
            border_islands[key] = True
            check_around(new_i, new_j, matrix, border_islands)

def removeIslands(matrix):
    border_islands = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and is_border(i, j, matrix):
                if make_key(i, j) in border_islands:
                    continue
                border_islands[make_key(i, j)] = True
                check_around(i, j, matrix, border_islands)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not make_key(i, j) in border_islands:
                matrix[i][j] = 0
    return matrix

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

output = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

print(removeIslands(matrix) == output)