



def graphMaker(edges):
    graph = {}
    for arr in edges:
        a = arr[0]
        b = arr[1]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def shortestpath(edges, src, dst):
    graph = graphMaker(edges)
    que = [[src, 0]]
    visited = {}
    while len(que):
        node , distence = que.pop(0)
        if node not in visited:
            visited[node] = True
            if node == dst:
                return distence
            for child in graph[node]:
                que.append([child, distence+1])
    return -1




edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
print(shortestpath(edges, 'b', 'g')) # 2
