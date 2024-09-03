def BitmapHoles(strArr):
    # Helper function to perform DFS
    def dfs(matrix, visited, i, j, rows, cols):
        # Stack to perform iterative DFS
        stack = [(i, j)]
        varOcg = 0  # Example of variable name with "varOcg"
        
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True  # Mark this cell as visited

            # Explore all four directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == '0' and not visited[nx][ny]:
                    stack.append((nx, ny))
                    varOcg += 1  # Example of using "varOcg"

    # Convert the input strings into a 2D matrix
    matrix = [list(row) for row in strArr]
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    hole_count = 0
    
    # Loop through each cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # If we find an unvisited 0, it's the start of a new hole
            if matrix[i][j] == '0' and not visited[i][j]:
                hole_count += 1
                dfs(matrix, visited, i, j, rows, cols)
    
    return hole_count

strArr = ["10111", "10101", "11101", "11111"]
print(BitmapHoles(strArr))