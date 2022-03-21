#
# def way1(logs):
#     dig = {}
#     let = {}
#
#     for log in logs:
#         label = ""
#         rest = ""
#         for i in range(len(log)):
#             if log[i] == " ":
#                 label = log[:i]
#                 rest = log[i+1:]
#                 break
#         if rest[0].isalpha():
#             if rest not in let :
#                 # print("its not here ")
#                 let[rest] = []
#
#             let[rest].append(label)
#
#         else :
#             # dig[rest] = label
#             digits.append(item)


def kk(n):
    return (n%2,n)
arr = [4,1,6,2,3,5]


print(sorted(arr,key(2)))


print(let)
    # ll = sorted(let.keys())
    res = []
    i = 0


    for key in ll:
        values = let[key]
        values = values.sort()
        for val in values:
            res.append(val + " " + key)
    print(res)



    for key, value in dig.items():
        res.append(value + " " + key)

    print(res)
    return res



# def way2(logs):
#     letters = {}
#     digits = []
#     for item in logs:
#         lst = item.split(" ")
#         if len(lst) > 1:
#             first = lst[1]
#             if ord('a') <= ord(first[0]) <= ord('z'):
#                 key = " ".join(lst[1:])
#                 if key not in letters:
#                     letters[key] = []
#                 letters[key].append(lst[0])
#             else:
#                 digits.append(item)
#
#     keys = list(letters)
#     keys.sort()
#     res = []
#
#     for key in keys:
#         letters[key].sort()
#         for idn in



logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
# way1(logs)
