
def way1(logs):
    dig = {}
    let = {}

    for log in logs:
        label = ""
        rest = ""
        for i in range(len(log)):
            if log[i] == " ":
                label = log[:i]
                rest = log[i+1:]
                break
        if rest[0].isalpha():
            let[rest] = label
        else :
            dig[rest] = label

    ll = sorted(let.keys())
    res = []
    i = 0
    while i < len(ll)-1:
        if ll[i] == ll[i+1]:
            j = i
            same = []
            while ll[j] == ll[j+1] and j<len(ll)-1:
                same.append(let[ll[j]]+" "+ll[j])
                j+=1
            same.append(let[ll[j]]+" "+ll[j])
            res += sorted(same)
            i = j
        else:
            res.append(let[ll[i]]+" "+ll[i])
        i += 1
    res.append(let[ll[i]]+" "+ll[i])
    print(res)



    for key, value in dig.items():
        res.append(value + " " + key)

    print(res)
    return res





logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
way1(logs)
