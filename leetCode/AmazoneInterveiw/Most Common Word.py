

def way1(paragraph, banned):
    dic = {}
    back = 0

    for i in range(len(paragraph)):
        if paragraph[i] == " ":
            word = paragraph[back:i]
            if '.' in word or ',' in word:
                word = word[:len(word)-1]
            if word not in dic:
                dic[word] = 0
            dic[word] += 1
            back = i+1

    word = paragraph[back:]
    if '.' in word or  ',' in word:
        word = word[:len(word)-1]
    if word not in dic:
        dic[word] = 0
    dic[word] += 1

    MAX = 0
    ww = ""
    for key, value in dic.items():
        if key not in banned:
            if MAX < value:
                MAX = value
                ww = key

    return ww


def way2(paragraph, banned):
    dic = {}

    paragraph = paragraph.lower()
    res = ""
    for i in paragraph:
        if  i.isalpha() or i==" ":
            res += i
        else:
            res += " "

    print(res)
    words = res.split(" ")

    for word in words:
        if word != "":
            if word not in dic:
                dic[word] = 1
            dic[word] += 1
    mm = ""
    max = 0
    for key,value in dic.items():
        if key not in banned:
            if value > max:
                max = value
                mm = key

    return mm


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
paragraph = paragraph.lower()

# print(paragraph)

paragraph = "a,a,a,a,         b,b,b,b,b,b,b               c,c c c c c "

banned = ['b']


# print(way1(paragraph, banned))
print(way2(paragraph, banned))