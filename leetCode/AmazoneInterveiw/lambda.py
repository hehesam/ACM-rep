def kk(n):
    return n%2, n
arr = [4,1,6,2,3,5]


print(sorted(arr,key=kk))



def prime_nums(num):
    primes = set()
    primes.add(2)
    i = 3
    while i < num:
        flag = False
        for prime in primes:
            if i % prime == 0:
                flag = True
                break
