def way1(strs):
    allword_dict = {}

    for word in strs:
        sorted_word = sorted(word)
        key = ""
        for i in sorted_word:
            key += i
        if key not in allword_dict:
            allword_dict[key] = []
        allword_dict[key].append(word)
    for i,j in allword_dict.items():
        print(i,j)
    res = []
    for val in allword_dict.values():
        res.append(val)
    return res


s = "cba"
print(sorted(s))


strs = ["eat","tea","tan","ate","nat","bat"]
print(way1(strs))