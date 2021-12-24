


def explore(graph, node, visited):
  if node in visited:
    return False
  visited[node] = True

  for child in graph[node]:
    explore(graph, child, visited)
  return True



def connectedComponentsCount(graph):
  visited = {}
  count = 0
  for node in graph.keys():
    if explore(graph, node, visited):
      print(visited)
      count+=1
  return count


graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}
res = connectedComponentsCount(graph)
print(res)
# for node in graph.keys():
#   print(node)