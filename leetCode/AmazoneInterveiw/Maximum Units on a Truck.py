
import time

def way1(boxTypes, truckSize):
    dd = {}
    for i in boxTypes:
        if i[1] not in dd:
            dd[i[1]] = 0
        dd[i[1]] += i[0]
    sumval = 0
    count = 0
    lastKey = num = -1
    for key in sorted(dd.keys(),reverse=True):
        if count >= truckSize:

            break
        count += dd[key]
        sumval += dd[key] * key
        lastKey = key
        num = dd[key]


    sumval -= lastKey*num
    count -= num
    for i in range(num):
        if count == truckSize:
            break
        count += 1
        sumval += lastKey
    return sumval


def way2(boxTypes, truckSize):
    boxTypes.sort(key = lambda x:x[1], reverse=True)
    total = 0
    for box in boxTypes:
        if box[0] <= truckSize:
            total += box[0] * box[1]
            truckSize -= box[0]

        else:
            total += truckSize * box[1]
            break
    return total

def way3(sleft, lst, res):
    if sleft < 0 :
        return
    if sleft == 0:
        res.append(lst)
        return
    for b in boxTypes:


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
ss  = time.time()
print(way1(boxTypes, truckSize))
print("way1: ", time.time()-ss)
ss = time.time()
print(way2(boxTypes, truckSize))
print("way2: ", time.time()-ss)
