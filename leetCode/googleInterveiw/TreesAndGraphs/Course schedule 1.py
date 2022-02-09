
def graph_maker(arr, size):
    graph = {}
    for i in range(size):
        graph[i] = []
    for a,b in arr:
        graph[a].append(b)
    return graph

def dfs(graph, parent, visited):
    if parent in visited:
        return False
    if graph[parent] == []:
        return True
    visited.add(parent)

    for child in graph[parent]:
        if not dfs(graph, child, visited) : return False

    visited.remove(parent)
    graph[parent] = []
    return True




numCourses = 4

prerequisites = [[1,0],[0,2],[2,3],[3,1]]

graph = graph_maker(prerequisites, numCourses)

flag = False
visited = set()
for key in graph.keys():
        if not dfs(graph, key, visited):
            print(False)
            flag = True
            break

if not flag :
    print(True)