
def allForms(wordList):
    combinations = {}
    for word in wordList:
        for i in range(len(word)):
            starword = word[:i]+'*'+word[i+1:]
            if starword not in combinations:
                combinations[starword] = []
            combinations[starword].append(word)
    return combinations


def iterate(wordList, str,stp, combination):
    que = [(str, 1)]
    visited = {}
    while len(que):
        print(que)
        current, distance = que.pop(0)
        visited[current] = True
        if current == stp:
            return distance
        for i in range(len(current)):
            starWord = current[:i]+'*'+current[i+1:]
            if starWord in combination:
                for x in combination[starWord]:
                    if x not in visited:
                        visited[x] = True
                        que.append((x,distance+1))
            else:
                return 0
    return 0



wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"
wordList.append(beginWord)
combination = allForms(wordList)
res = iterate(wordList, beginWord, endWord, combination)
print(res)
# print(letter_iterator(alph, wordList, beginWord,endWord))












