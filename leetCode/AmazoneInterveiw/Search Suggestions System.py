
def way1(products, searchWord):
    products = sorted(products)

    lres = []
    res = ""
    index = 0

    for s in searchWord:

        tmp = []
        res += s
        i = index

        while i < len(products):
            if res in products[i]:
                length = 3

                if i+ length > len(products):
                    length = len(products)

                for j in range(length):
                    if res in products[j]:
                        tmp.append(products[j])
                lres.append(tmp)
                tmp = []
                index = i
                break


            i += 1

    if len(lres) == 0:
        for i in range(len(searchWord)):
            lres.append([])
    return lres

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

# products = ["havana"]
# searchWord = "havana"
#
# products = ["bags","baggage","banner","box","cloths"]
# searchWord = "bags"
#
products = ["havana"]
searchWord = "tatiana"

print(way1(products, searchWord))

