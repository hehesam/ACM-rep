

def breaker(s, wordDict):

    i = 0
    while i < len(s):

        for word in wordDict:

            if s[i] == word[0]:
                if s[i:i+len(word)] == word:
                    s_part =  s[i+len(word):]
                    res = breaker(s_part, wordDict)
                    if res:
                        return res
                    else :
                        # i = -1
                        continue
                    # i = -1
                    # break

        i += 1


    if len(s) == 0:
        return True
    else:
        return False



def DP(s, wordDict):

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for word in wordDict:
            if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                dp[i] = dp[i+len(word)]
            if dp[i]:
                break

    return dp[0]

def DP2(s, wordDict):
    dp = [False for i in range(len(s)+1)]
    dp[0] = True

    for i in range(0,len(s)+1):
        for word in wordDict:
            if i + len(word) <= len(s) :
                if s[i:i+len(word)] == word:
                    dp[i+len(word)] = dp[i]

    return dp[len(s)]


s = "leetcode"
wordDict = ["leet","code"]

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
#
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# s = "cars"
# wordDict = ["car","ca","rs"]
#
# s = "applepenapple"
# wordDict = ["apple","pen"]
# #
# s = "bb"
# wordDict = ["a","b","bbb","bbbb"]
# s = 'hesamsamsamsamhesam'
# wordDict = ['b']

# print(breaker(s, wordDict))

print(DP2(s, wordDict))