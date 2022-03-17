import  string

# index[26][2] record last two occurrence index for every upper characters.
# Initialise all values in index to -1.
# Loop on string S, for every character c, update its last two occurrence index to index[c].
# Count when loop. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
# For the first "A": (6-3) * (3-(-1))"
# For the second "A": (9-6) * (6-3)"
# For the third "A": (N-9) * (9-6)"

def way1(S):
    index = {c: [-1, -1] for c in string.ascii_uppercase}
    res = 0
    for i, c in enumerate(S):
        k, j = index[c]
        res += (i - j) * (j - k)
        index[c] = [j, i]
    for c in index:
        k, j = index[c]
        res += (len(S) - j) * (j - k)
    return res % (10**9 + 7)

#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------


# "res[i]" means the result of all substrings ended at index "i". Final result is sum of all "res[i]"
# res[i] will be composed by all substrings of res[i-1] appending "i". For each substring in res[i-1], when we append "i" to it:
#
# If there is no "i" in this substring, e.g.,
# append "A" to "B", substring changes from "B" to "BA",
# the UNIQ value of this substring changes from 1 to 2,
# we add 1 to all this kind of substrings.


# If there is one "i" in this substring, e.g. append "A" to "AB",
# substring changes from "AB" to "ABA",
# the substring UNIQ value changes from 2 to 1.
# We minus 1 to this kind of substrings.


# If there is more than one "i" in this substring, e.g. append "A" to "ABAB",
# substring changes from "ABAB" to "ABABA", the substring UNIQ value doesn't change.
# We do nothing to this kind of substrings.


# So for each new "i", we only care how many same char before it, and what are the indexes of these chars.
# Actually we only need to know 2 same chars before it. Because situations more than 2 chars can be handled the same as 2 chars.

def way2(S):
    res=[0]*(len(S)+1)
    idxs=[[-1,-1]]*26
    for i,c in enumerate(S):
        code=ord(c)-ord('A')
        first,second=idxs[code]
        res[i+1]=1+res[i]+(i-1-second)-(second-first)
        idxs[code]=[second,i]
    # return sum(res)%(10**9+7)
    return sum(res)

s = "LEETCODE"
s = "ABC"


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------



# brute force O(n^3)

def countUniqueChars(s):
    all = set()
    banned = set()
    full = ""
    for i in s:
        if i in banned:
            continue
        if i in all :
            all.remove(i)
            banned.add(i)
        else:
            all.add(i)

    return len(all)


def way3(s):
    sum = 0
    allSub = set()
    for i in range(len(s)):
        j = i +1
        while j <= len(s):
            sum += countUniqueChars(s[i:j])
            # print(sum)
            j+=1

    return sum

s = "LEETCODE"
print(way1(s),way2(s), way3(s))


