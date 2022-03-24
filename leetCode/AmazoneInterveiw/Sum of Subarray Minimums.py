


# brute force
def way1(arr):
    sum = 0
    # for i in range(len(arr)):
    #     for j in range(i, len(arr)):
    #         sum += min(arr[i:j+1])

    tmp = []
    i = 0
    while i < len(arr):
        min_val = arr[i]
        j = i
        while j<len(arr):
            min_val = min(min_val, arr[j])
            sum += min_val
            j+=1
        i += 1

    return sum

def way2(arr):
    # stack :
    s1 = []
    s2 = []
    n = len(arr)
    next_smaller = []*n
    pre_smaller = []*n
    for i in range(n):
        next_smaller.append(n-i-1)
        pre_smaller.append(i)

    for i in range(n):
        while len(s1) != 0 and arr[s1[-1]] > arr[i]:
            next_smaller[s1[-1]] = i - s1.pop()-1

        s1.append(i)

    for i in range(n,-1,-1):
        while len(s2) != 0 and arr[s2[-1]] >= arr[i]:
            pre_smaller[s2[-1]] = s2.pop()-i-1


        s2.append(i)

    ans = 0
    for i in range(n):
        ans += arr[i]*(pre_smaller[i]+1)*(next_smaller[i]+1)

    return ans
arr = [3,1,2,4]
# arr = [11,81,94,43,3]
print(way2(arr))