






# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927522/Python-n-log-n-690-ms

def way1(inventory, orders):

    inventory.sort(reverse=True)

    inventory.append(0)

    res = 0
    index = 0
    width = 0

    while orders > 0:
        width += 1

        sell = min(orders, width*(inventory[index]-inventory[index+1]))
        whole, remainder = divmod(sell, width)
        res += width * (whole*(inventory[index]+inventory[index]-(whole-1)))//2 + remainder*(inventory[index]-whole)

        orders -= sell

        index += 1


    return res


# another way is to yse heap tree like this every time we add the largest number from the top of heap tree














inventory = [2,5]
orders = 4

inventory = [7,4,3]
orders = 9

print(way1(inventory, orders))