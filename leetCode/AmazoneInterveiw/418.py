
import time

def sum(num):
    res = 0
    while num :
        a = num%10
        res += a**2
        num //= 10
    return res

def converging(n):
    dic = {}
    while 1:


        if n == 1:
            return True

        n = sum(n)

        if n in dic:
            return False
        dic[n] = True




n =19


# print(converging(13))

c = ''
s1 = time.time()
for i in range(9999999):
    c += 'C'
print('->', time.time()-s1)

s1 = time.time()
a = c[9999997:9999998]
print("->", time.time()-s1)