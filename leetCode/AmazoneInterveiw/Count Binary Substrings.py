def way1(s):

    arr = []
    flag = s[0]
    tmp = ""
    for i in s:
        if flag != i:
            flag = i
            arr.append(tmp)
            tmp = ""
        tmp += i
        print(arr)
    arr.append(tmp)
    print(arr)
    count = 0
    for i in range(1,len(arr)):
        count += min(len(arr[i-1]), len(arr[i]))
    print(arr)

    return count

def way2(s):
    flag1 = s[0]
    flag2 = 0
    left = ""
    right = ""
    count = 0
    for i in s:
        if flag1 != i:


            if flag2 == 1:
                count += min(len(right), len(left))

            flag1 = i
            flag2 = 1
            left = right
            right = ""

        right += i

    count += min(len(right), len(left))
    return count


s = "00110011"
# s = "10101"
print(way2(s))