








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





def way2(username, timestamp, website):
    users = {}
    for user, time , site in sorted(zip(username, timestamp, website), key=lambda x:(x[0], x[1])):
        if user not in users:
            users[user] = []
        users[user].append(site)

    for k,v in users.items():
        print(k,v)


    patterns = {}

    for value in users.values():
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

    return max(sorted(patterns), key=patterns.get)





def way3(username, timestamp, website):
### sort the data according to time stamp. zip ensure username and website get swapped to corresponding location
    tupled_data = sorted(zip(username, timestamp, website), key = lambda x: x[1])


### as the data is sorted based on timestamp.
#   Appending the data to the users list will ensure correct order of website visits for the user.
    formated_data = {}
    for u, _, w in tupled_data:
        if u not in formated_data:
            formated_data[u] = []
        formated_data[u].append(w)

### for each user visit all the possible patterns and add the counts to the dict.
#   Ensure you only count a pattern for single user only once. Done by using seen set.

    patterns = {}
    for u in formated_data:
        seen =set()
        n = len(formated_data[u])
        ### form all the possible patterns for the current user. Add it to pattern is not in seen.
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    p = (formated_data[u][i], formated_data[u][j], formated_data[u][k])
                    if p not in seen:
                        seen.add(p)
                        if p not in patterns:
                            patterns[p] = 0
                        patterns[p] += 1



### find the keys having max value. Use list comprehension to select the keys with value equal to max_value
    max_value = max(patterns.values())
    keys_with_max_value =[items[0] for items in patterns.items() if items[1] == max_value]


### lexicographical sorting
    return list(sorted(keys_with_max_value)[0])





username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]



# username = ["dowg","dowg","dowg"]
# timestamp = [158931262,562600350,148438945]
# website = ["y","loedo","y"]
username = ["ua","ua","ua","ub","ub","ub"]
timestamp = [1,2,3,4,5,6]
website = ["a","b","a","a","b","c"]


username = ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
timestamp = [436363475,710406388,386655081,797150921]
website = ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]
# ["oz","mryxsjc","wlarkzzqht"]
print(sorted(website))
print(way3(username, timestamp, website))