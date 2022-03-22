








def way1(username, timestamp, website):

    all = {}
    for i in range(len(timestamp)):
        all[timestamp[i]] = (username[i], website[i])

    for i,j in sorted(all.items()):
        print(i,j)

    each = {}
    for key in sorted(all.keys()):
        user,web = all[key]
        if user not in each:
            each[user] = []
        each[user].append(web)



    for i,j in each.items():
        print(i,j)

    patterns = {}
    for value in each.values():
        i = 0
        while i <= len(value) - 3:
            patt = ""
            # print(value[i:i+3])
            for word in value[i:i+3]:
                patt += word + " "
            patt = patt[:-1]

            if patt not in patterns:
                patterns[patt] = 0
            patterns[patt] += 1
            i+=1

    for i,j in patterns.items():
        print(i,j)


    sort_keys = sorted(patterns.keys())
    max_count = 0
    res = []
    for key in sort_keys:
        if max_count < patterns[key]:
            max_count = patterns[key]
            res = key.split(" ")
    return res




# def way2(username, timestamp, website):







username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]



# username = ["dowg","dowg","dowg"]
# timestamp = [158931262,562600350,148438945]
# website = ["y","loedo","y"]
# username = ["ua","ua","ua","ub","ub","ub"]
# timestamp = [1,2,3,4,5,6]
# website = ["a","b","a","a","b","c"]


username = ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
timestamp = [436363475,710406388,386655081,797150921]
website = ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]
# ["oz","mryxsjc","wlarkzzqht"]
print(sorted(website))
print(way1(username, timestamp, website))