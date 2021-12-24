


def DFS(graph, source):
    stack = []
    stack.append(source)
    while(len(stack)):
        res = stack.pop()
        print(res)
        children = graph[res]
        for child in children:
            stack.append(child)

def DFS_recursion1(graph, stack):
        if len(stack) == 0:
            return
        res = stack.pop()
        print(res)
        children = graph[res]
        for child in children:
            stack.append(child)
            DFS_recursion1(graph, stack)

def DFS_recursion2(graph, source):
    print(source)
    if len(graph[source]) == 0:
        return
    children = graph[source]
    for child in children:
        DFS_recursion2(graph, child)

def BFS(graph, source):
    qu = []
    qu.append(source)
    while len(qu):
        res = qu.pop(0)
        print(res)
        children = graph[res]
        for child in children:
            qu.append(child)


graph = {'a': ['b', 'c'],
         'b': ['d'],
         'c': ['e'],
         'd': ['f'],
         'e': [],
         'f': []}

print('DFS using stack: ')
DFS(graph, 'a')

stack = ['a']
print('DFS recursion 1')
DFS_recursion1(graph, stack)
print('DFS recursion 2')
DFS_recursion2(graph, 'a')
print('\nBFS queuee')
BFS(graph, 'a')