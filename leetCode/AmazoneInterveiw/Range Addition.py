


# brute force
def way1(length,updates):
    arr = [0]* length
    for part in updates:
        x,y,val = part
        for i in range(x,y+1):
            arr[i] += val

    print(arr)
    return arr


def way2(lengt, updates):
    res = [0] * length

    for part in updates:
        start = part[0]
        end = part[1]
        val = part[2]

        res[start] += val
        if end < length-1:
            res[end+1] -= val
        print(res)
    tmp = res.copy()
    print()
    for i in range(1,length):
        print(res)
        res[i] = res[i-1] + tmp[i]

    return res


length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]


length = 10
updates = [[2,4,6],[5,6,8],[1,9,-4]]

print(way2(length, updates))