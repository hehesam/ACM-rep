import time


def printer(dp):

    for i in dp:
        print(i)

def longestPalindrome(s):

    ss = time.time()
    if s is "":
        return s
    res = ""
    dp = [[None for i in range(len(s))] for j in range(len(s))]
    for j in range(len(s)):
        for i in range(j+1):
            if i == j:
                dp[j][i] = True
            elif j == i+1:
                dp[j][i] = (s[i] == s[j])
            else:
                dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
            if dp[j][i] and j - i + 1 > len(res):
                res = s[i:j+1]
        # printer(dp)
        # print('\n\n')

    print("the time is :", time.time() - ss)
    return res


def making_matrix(s):
    matrix = []
    for i in s:
        xx = []
        for j in s:
            xx.append(None)
        matrix.append(xx)
    return matrix


def DP(s):

    ss = time.time()
    # mat = making_matrix(s)
    mat = [[None for j in range(len(s))] for i in range(len(s))]
    pluser = 0
    max = ""

    for i in range(len(mat)):
        for i in range(len(mat)):
            x = i
            y = i+pluser

            if y < len(s):
                if s[x] == s[y]:
                    if pluser < 2:
                        mat[x][y] = 1
                        res = s[x:y+1]
                        # print(res)
                        if len(res) > len(max):
                            max = res
                    else :
                        if mat[x+1][y-1] == 1:
                            mat[x][y] = 1
                            res = s[x:y + 1]
                            # print(res)
                            if len(res) > len(max):
                                max = res
                        else:
                            mat[x][y] = 0
                else:
                    mat[x][y] = 0

        pluser += 1
    # printer(mat)
    print('my code time : ', time.time()-ss)
    return max


def left_right(s):
    ss = time.time()
    res = ""
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

    print('left and right time : ', time.time()-ss)
    return res
s = "babad"
s = ""
for i in range(1000):
    s += 'c'
# s = "twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqql" \
#     "rcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"

print(len(s))
print(longestPalindrome(s))
print(DP(s))
print(left_right(s))

