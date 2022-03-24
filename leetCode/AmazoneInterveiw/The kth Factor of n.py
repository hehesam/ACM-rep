from numpy import sqrt
import heapq
# brute force O(n)
def way1(n,k):


    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
        if count == k:
            return i
    return -1


# O(sqrt(n))

def way2(n, k):
    f1, f2 = [], []
    for s in range(1, int(sqrt(n)) + 1):
        if n % s == 0:
            f1 += [s]
            f2 += [n // s]

    if f1[-1] == f2[-1]:
        f2.pop()

    factors = f1 + f2[::-1]
    return -1 if len(factors) < k else factors[k - 1]


def heappush_k(num ,heap):
    heapq.heappush(heap, -num)
    if len(heap) > k:
        heapq.heappop(heap)

def way3(n,k):
    heap = []
    for x in range(1,int(n**0.5)+1):

        heappush_k(x,heap)

        if x != n//x:
            heappush_k(n//x,heap)

    if k == len(heap):
        return -heapq.heappop(heap)
    else :
        return -1
    # return -heapq.heappop(heap) if k == len(heap) else -1
n = 12
k = 3
n=7
k=2
# n =4
# k = 4
print(way3(n,k))