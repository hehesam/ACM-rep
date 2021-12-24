def buildGraph(edges):
        graph = {}
        for edge in edges:
            a, b = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph


def hasPath(graph, src, dst, Set):
    if src == dst:
        return True
    Set[src] = True
    for child in graph[src]:
        if child not in Set:
            if hasPath(graph, child, dst, Set):
                return True

    return False

def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, Set={})


# edges = [
#     ['i', 'j'],
#     ['k', 'i'],
#     ['m', 'k'],
#     ['k', 'l'],
#     ['o', 'n']
# ]

edges = [
  ['b', 'a'],
  ['c', 'a'],
  ['b', 'c'],
  ['q', 'r'],
  ['q', 's'],
  ['q', 'u'],
  ['q', 't'],
]
print(undirectedPath(edges, 'r', 'b'))