
def hasPath_DFS(graph, src, dst):
    if src == dst:
        return True

    for child in graph[src]:
        if hasPath_DFS(graph, child, dst):
            return True
    return False

def hasPath_BFS(graph, src, dst):
    qu = []
    qu.append(src)
    while len(qu):
        current = qu.pop(0)
        if current == dst:
            return True

        for child in graph[current]:
            qu.append(child)
    return False



graph = {'f': ['g', 'i'],
         'g': ['h'],
         'h': [],
         'i': ['g', 'k'],
         'j': ['i'],
         'k': []}


print(hasPath_DFS(graph, 'f', 'k'))
print()
print(hasPath_BFS(graph, 'f', 'k'))