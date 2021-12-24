

def lookAround(grid, corr, visited):
  x,y = corr
  if 0<=x<len(grid) and 0<=y<len(grid[x]):
    if corr not in visited and grid[x][y] == 'L':
      visited[corr] = True
      count = 1
      # up
      count += lookAround(grid, (x-1,y), visited)
      # down
      count += lookAround(grid, (x+1,y), visited)
      # left
      count += lookAround(grid, (x,y-1), visited)
      # right
      count += lookAround(grid, (x,y+1), visited)

      return count

  return 0


def minimumIsland(grid):
  visited = {}
  min = 999
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      corr = (x,y)
      if corr not in visited and grid[x][y] == 'L':
        size = lookAround(grid, corr, visited)
        if size < min :
          min = size
  return min




grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

print(minimumIsland(grid))
