
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


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------


# In a sorted list of words,
# for any word A[i],
# all its sugested words must following this word in the list.
#
# For example, if A[i] is a prefix of A[j],
# A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]



import bisect
def way2(products, searchWord):
    products.sort()
    res, prefix, i = [], '', 0
    for c in searchWord:
        prefix += c

        i = bisect.bisect_left(products, prefix)
        # Locate the insertion point for prefix in products to maintain sorted order.

        tmp = []
        for w in products[i:i+3]:
            if w.startswith(prefix):
                tmp.append(w)
        res.append(tmp)
        # res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
    return res

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

# products = ["havana"]
# searchWord = "havana"
#
# products = ["bags","baggage","banner","box","cloths"]
# searchWord = "bags"
# #
# products = ["havana"]
# searchWord = "tatiana"

# print(way1(products, searchWord))
print(way2(products, searchWord))

