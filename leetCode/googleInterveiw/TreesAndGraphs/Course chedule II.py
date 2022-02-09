





# IT seems that bfs is not working for this problem
def BFS(graph):
    res = {}
    visited = {}
    que = []

    for key in graph.keys():
        if key not in visited:
            que.append(key)


        while len(que):
            current = que.pop(0)

            visited[current] = True
            if current not in res:
                res[current] = True
            if current in graph:
                for node in graph[current]:
                    if node in visited and current in graph[node]:
                        return []
                    que.append(node)

    return list(res.keys())


def making_directed_graph(arr, size):
    graph = {}
    for i in range(size):
        graph[i] = []
    for x,y in arr:
        # if y not in graph:
        #     graph[y] = []
        graph[y].append(x)

    return graph

def DFS(graph, parent, visited, res ):
    if parent in visited and graph[parent] == []:
        return True
    if parent in visited and graph[parent] != []:
        res = []
        return False

    visited[parent] = True
    for child in graph[parent]:
        if not DFS(graph, child, visited, res):
            return False
    graph[parent] = []
    res.append(parent)

    return True


numCourses = 4

prerequisites = [[1,0],[2,0],[3,1],[3,2]]

graph = making_directed_graph(prerequisites, numCourses)

# a = 0
print(graph)
#
# print(BFS(graph))


visited = {}

myLife = []

for key in graph.keys():
    if key not in visited:
        res = []

        if not DFS(graph, key ,visited, res):
            myLife = []
            break

        myLife += res

        print(myLife)


myLife.reverse()
print(myLife)