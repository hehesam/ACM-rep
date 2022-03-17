def countUniqueChars(s):
    all = set()
    banned = set()
    full = ""
    for i in s:
        if i in banned:
            continue
        if i in all :
            all.remove(i)
            banned.add(i)
        else:
            all.add(i)

    return len(all)


def subSet(s):
    sum = 0
    allSub = set()
    for i in range(len(s)):
        j = i +1
        while j <= len(s):
            sum += countUniqueChars(s[i:j])
            # print(sum)
            j+=1

    return sum



s = "LEETCODE"
s = "ABC"


def aa(arr):
    base = 0
    res = []
    for i in arr:
        base += i
        res.append(base)
    return res


def aa2(arr):
    base = 0
    res = []
    for i in range (len(arr)):
        base += arr[i]
        res.append(base)
    return res

def aa3(arr):
    base = 0
    res = []
    i = 0
    while i < len(arr):
        base += arr[i]
        res.append(base)
        i += 1
    return res


from itertools import accumulate
import time
import random

a = [1]*9999

ss = time.time()
acc = accumulate(a)
print(list(acc))
print("accumulate : ", time.time()-ss)

ss = time.time()
print(aa(a))
print("aa : ", time.time()-ss)

ss = time.time()
print(aa2(a))
print("aa2 : ", time.time()-ss)

ss = time.time()
print(aa3(a))
print("aa3 : ", time.time()-ss)

