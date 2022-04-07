def way1(s1,s2):
    lst1 = s1.split('.')
    lst2 = s2.split('.')
    n = min(len(lst1), len(lst2))
    for i in range(n):
        var_left = int(lst1[i])
        var_right = int(lst2[i])
        if var_left > var_right:
            return 1
        if var_left < var_right:
            return -1

    return 0


version1 = "1.01"
version2 = "1.001"

version1 = "0.1"
version2 = "1.1"
print(way1(version1,version2))
