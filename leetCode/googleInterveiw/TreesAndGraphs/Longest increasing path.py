


def count_path(matrix,curr, past, visited):

    x,y = curr

    if curr in visited:
        if matrix[x][y] > past:
            return visited[curr]

    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > past:
        sum = 1
        # up
        sizes = []
        sizes.append(count_path(matrix, (x-1,y), matrix[x][y], visited))
        # down
        sizes.append(count_path(matrix, (x+1,y), matrix[x][y], visited))
        # left
        sizes.append(count_path(matrix, (x,y-1), matrix[x][y], visited))
        # right
        sizes.append(count_path(matrix, (x,y+1), matrix[x][y], visited))

        visited[curr] = sum + max(sizes)
        return sum + max(sizes)

    return 0

def count_path2(matrix, curr):
    i,j = curr
    que = []
    que.append((i,j,0,-1))

    max_dis = 0
    while len(que):
        x,y,dis,past = que.pop(0)
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > past:
            dis += 1
            past = matrix[x][y]
            # up
            que.append((x-1,y,dis,past))
            #down
            que.append((x+1,y,dis,past))
            #left
            que.append((x,y-1,dis,past))
            #right
            que.append((x,y+1,dis,past))

        elif dis > max_dis  and 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] <= past:
            max_dis = dis
    return max_dis



def max_path(matrix):
    max_way = 0
    visited = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            curr = (i,j)
            res = count_path(matrix, curr, -1, visited)
            # res = count_path2(matrix, curr)
            if res > max_way:
                max_way = res

    return max_way






# matrix = [[9,9,4],[6,6,8],[2,1,1]]

# matrix = [[5,6,7],[4,9,8],[3,2,1]]

matrix = [[0,1,2,3,4,5,6,7,8,9],
          [19,18,17,16,15,14,13,12,11,10],
          [20,21,22,23,24,25,26,27,28,29],
          [39,38,37,36,35,34,33,32,31,30],
          [40,41,42,43,44,45,46,47,48,49],
          [59,58,57,56,55,54,53,52,51,50],
          [60,61,62,63,64,65,66,67,68,69],
          [79,78,77,76,75,74,73,72,71,70],
          [80,81,82,83,84,85,86,87,88,89],
          [99,98,97,96,95,94,93,92,91,90],
          [100,101,102,103,104,105,106,107,108,109],
          [119,118,117,116,115,114,113,112,111,110],
          [120,121,122,123,124,125,126,127,128,129],
          [139,138,137,136,135,134,133,132,131,130],
          [0,0,0,0,0,0,0,0,0,0]]

print(max_path(matrix))