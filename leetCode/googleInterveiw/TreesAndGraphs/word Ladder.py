def pairWords(s1, s2):
    if len(s1) != len(s2):
        return False
    count = 0
    for i in range(len(s1)):
        if s2[i] != s1[i]:
            count += 1
    if count > 1 or count == 0:
        return False
    else:
        return True


def graphMaker(wordList):
    graph = {}
    for word in wordList:
        if word not in graph:
            graph[word] = []
        for w in wordList:
            if pairWords(word, w):
                if w not in graph[word]:
                    graph[word].append(w)
                    if w not in graph:
                        graph[w] = []
                    graph[w].append(word)
    return graph


def shortestPath(graph, a, b):
    count = 0
    que = []
    que.append(a)
    while len(que):
        count += 1
        current = que.pop(0)
        if current == b:
            return count
        for i in graph[current]:
            que.append(i)


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        wordList.append(beginWord)

        graph = graphMaker(wordList)
        print(graph)
        print(shortestPath(graph, beginWord, endWord))

















