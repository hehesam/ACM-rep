def way1(s):
    uniq = set()
    nouniq = set()
    for i in s:
        if i in uniq or i in nouniq:
            uniq.remove(i)
            nouniq.add(i)
        else:
            uniq.add(i)


    for i in range(len(s)):
        if s[i] in uniq:
            return i
    return -1


s = "leetcode"