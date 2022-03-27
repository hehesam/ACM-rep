


# a function to check the condition of surranding cells
def condition(grid,x,y):
    if 0<=x<len(grid) and 0<=y<len(grid[x]):
        if grid[x][y] == 1:
            return True
    return False



# we use BFS
def way1(grid):

    visited = set()
    qu = []

    # first we find the day 0 rotten oranges
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                qu.append((i,j,0))

    res = 0

    while len(qu):
        x,y,day = qu.pop(0)
        # down
        if condition(grid, x+1,y):
            # change it to rotten
            grid[x+1][y] = 2
            qu.append((x+1,y,day+1))
        # up
        if condition(grid, x-1,y):
            # change it to rotten
            grid[x-1][y] = 2
            qu.append((x-1,y,day+1))

        # right
        if condition(grid, x,y+1):
            # change it to rotten
            grid[x][y+1] = 2
            qu.append((x,y+1,day+1))

        # left
        if condition(grid, x,y-1):
            # change it to rotten
            grid[x][y-1] = 2
            qu.append((x,y-1,day+1))

        res = day


    # finaly we check for any fresh orange
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return -1

    return res


grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]

print(way1(grid))