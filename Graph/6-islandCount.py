
def checkAround(grid, corr,visited):
  x,y = corr
  if 0<=x<len(grid) and 0<= y < len(grid[x]):
      if grid[x][y] == 'L' and corr not in visited:
            visited[(x,y)] = True
            # up
            checkAround(grid, (x-1, y), visited)
            # down
            checkAround(grid, (x+1, y), visited)
            #right
            checkAround(grid, (x, y+1), visited)
            #left
            checkAround(grid, (x, y-1), visited)

            return 1





def adjacency(grid):
    visited = {}
    count = 0
    for x in range(len(grid)):
      for y in range(len(grid[x])):
        corr = (x, y)
        if grid[x][y]=='L' and corr not in visited:

            count += checkAround(grid, corr, visited)

    return count


grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

print(adjacency(grid))