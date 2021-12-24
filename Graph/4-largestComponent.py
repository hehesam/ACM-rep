

def explorSize(graph, current, visited):
  if current in visited:
    return 0
  visited[current] = True
  size = 1
  for node in graph[current]:
    size += explorSize(graph, node, visited)

  return size



def largestComponent(graph):
  max = 0
  visited = {}
  for node in graph.keys():
    size = explorSize(graph, node, visited)
    if size > max:
      max = size
  return max

graph = {
  0: ['4', '7'],
  1: [],
  2: [],
  3: ['6'],
  4: ['0'],
  6: ['3'],
  7: ['0'],
  8: []
}
for key , value in graph.items():
  graph[key] = list(map(int, value))

print(graph)

print(largestComponent(graph))