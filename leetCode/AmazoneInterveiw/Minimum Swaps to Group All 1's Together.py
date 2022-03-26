
#brute force

def way1(data):
    ones,zero = 0,0
    for i in data:
        if i == 1:
            ones += 1
        else:
            zero +=1

    min_num = zero


    for i in range(len(data)-ones+1):
        j = i
        count = 0
        while j < i+ones:
            if data[j] == 0:
                count += 1
            j += 1
        print(count)

        min_num = min(min_num, count)

    return min_num



# O(N)
def way2(data):
    zero,one = 0,0
    for i in data:
        if i:
            one += 1


    base = 0

    for i in range(one):
        tmp = base
        if data[i] == 0:
            zero += 1



    base = zero
    for i in range(one, len(data)):
        print("index", i-1, i+one-1)
        if data[i-one] == 0:
            zero -= 1
        if data[i] == 0:
            zero += 1
        base = min(zero, base)
    return base


data = [1,0,1,0,1,0,0,1,1,0,1]
data = [0,0,0,1,0]
data = [1,0,1,0,1]
# data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
# data = [1,0,0,1,1,1]
print(way1(data), way2(data))