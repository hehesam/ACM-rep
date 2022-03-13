

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


s = "leetcode"
wordDict = ["leet","code"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

# s = "cars"
# wordDict = ["car","ca","rs"]
#
# s = "applepenapple"
# wordDict = ["apple","pen"]
# #
# s = "bb"
# # wordDict = ["a","b","bbb","bbbb"]
# s = 'hesamsamsamsamhesam'
# wordDict = ['b']

print(breaker(s, wordDict))