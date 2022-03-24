

# brute force
def way1(words):
    all = {}
    for i in words:
        for j in words:
            if i in j and not i == j:
                if j not in all:
                    all[j] = []
                all[j].append(i)

    # for i,j in all.items():
    #     print(i,j)

    res = []
    for key,val in all.items():
        tmp = key
        i = 0
        while i < len(val):
            for j in range(i,len(val)) :
                tmp = tmp.replace(val[j],"")
                # print(tmp)
            if len(tmp) == 0:
                res.append(key)
                break
            else:
                tmp = key

            i += 1
    return res





def dfs(word, words):
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        print(prefix,suffix)
        if prefix in words and suffix in words:
            return True
        if prefix in words and dfs(suffix, words):
            return True
        if suffix in words and dfs(prefix, words):
            return True
    return False


def way2(words):
    words = set(words)
    print(words)
    res = []
    for word in words :
        if dfs(word, words):
            res.append(word)

    return res

words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

# words = ["cat","dog","catdog"]

print(way2(words))