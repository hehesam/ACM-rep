

def BS(prices):

    low = prices[0]
    max_diff = 0

    for price in prices:
        if price < low:
            low = price
        else:
            if max_diff < price - low:
                max_diff = price-low

    return max_diff




prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
prices = [1,10,2,3,4,5]

print(BS(prices))