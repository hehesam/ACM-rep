




def way1(coins , amount):
    # dp = [[0] + [1] * (amount)] * len(coins)
    dp = [[0 for i in range(amount+1)] for j in range(len(coins))]



    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i==0:
               if j % coins[i] == 0:
                   dp[i][j] = j // coins[i]
                   # print(i, j)
               else:
                   dp[i][j] = -1

            elif coins[i] <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    #         print("-----------")
    #         print(dp[i])
    #
    for i in dp:
            print(i)

    return dp[-1][-1]



def way2(coins, amount):
    dp = [0] + [amount+1] * (amount)
    # print(dp)

    for i in range(len(coins)):
        for j in range(amount+1):
            if coins[i] <= j:
                dp[j] = min(dp[j-coins[i]] + 1, dp[j])
        print(dp)


    if dp[amount] == amount+1 : return -1
    else: return dp[amount]


coins = [1,3,6]
amount = 9

coins = [1,5,10]
amount = 10

# coins = [1,2,5]
# amount = 9

coins = [1,3,4,5]
amount = 7
coins = [2,5,10,1]
amount = 27

coins = [2]
amount = 3

# coins = [1]
# amount = 0

coins = [186,419,83,408]
amount = 6249

# dp = [[0] + [1] * (amount)] * len(coins)

# coins.sort()
#
# print(0%3)

#
print(way2(coins, amount))