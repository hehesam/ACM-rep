

def grid_search(grid, current,  visited):
    i , j = current
    if i<len(grid) and j<len(grid[i]) and grid[i][j] == '1' and current not in visited:
        visited[current] = True
        #up
        grid_search(grid, (i-1,j), visited)
        #down
        grid_search(grid, (i + 1, j), visited)
        #left
        grid_search(grid, (i, j-1), visited)
        #right
        grid_search(grid, (i, j+1), visited)
    return 1


def island_finder(grid):
    visited = {}
    count = 0
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            if (i,j) not in visited and grid[i][j] == '1':
                current = (i,j)
                count += grid_search(grid, current, visited)
    return count

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(island_finder(grid))