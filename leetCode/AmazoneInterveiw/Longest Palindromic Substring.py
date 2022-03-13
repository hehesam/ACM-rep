
import time





def making_matrix(s):
    ss = time.time()
    matrix = []
    dic = {}
    for i in s:
        xx = []
        for j in s:
            # xx.append(None)
            dic[(i,j)] = None
        # matrix.append(xx)
    ee = time.time()
    print("making matrix time is :", ee-ss)
    # return matrix
    return dic

def printer(mat):
    for i in mat:
        print(i)

def DP(mat, s):

    ss = time.time()

    pluser = 0
    max = ""

    for i in range(len(s)):
        for i in range(len(s)):
            x = i
            y = i+pluser

            if y < len(s):
                if s[x] == s[y]:
                    if pluser < 2:
                        # mat[x][y] = 1
                        mat[(x,y)] = 1
                        res = s[x:y+1]
                        # print(res)
                        if len(res) > len(max):
                            max = res
                    else :
                        if mat[(x+1,y-1)] == 1:
                            mat[(x,y)] = 1
                            res = s[x:y + 1]
                            # print(res)
                            if len(res) > len(max):
                                max = res
                        else:
                            mat[(x,y)] = 0
                else:
                    mat[(x,y)] = 0

        pluser += 1
    # printer(mat)

    ee = time.time()
    print("DP : ", ee-ss)

    print(len(max))
    return max






s = "aaaabbaa"

s = "babad"


s = 'cbbd'

s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"



print(len(s))
mat = making_matrix(s)

print(DP(mat,s))


# print(making_matrix(s))


