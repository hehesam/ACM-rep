def finding_islands(visited, grid, curr):
    x,y = curr
    if 0<=x<len(grid) and 0<=y<len(grid[x]) and grid[x][y] == "1" and curr not in visited:
        visited.add(curr)
        # left
        finding_islands(visited, grid, (x,y-1))
        # right
        finding_islands(visited, grid, (x,y+1))
        # up
        finding_islands(visited, grid, (x-1,y))
        # down
        finding_islands(visited, grid, (x+1,y))

        return True

    return

def makign_graph(grid):
    visited = set()
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "1" and (x,y) not in visited:
                if finding_islands(visited, grid, (x,y)):
                    count += 1

    return count



grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(makign_graph(grid))