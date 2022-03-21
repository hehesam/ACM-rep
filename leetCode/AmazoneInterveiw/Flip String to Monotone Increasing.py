

def compare(s1,s2):
    counter = 0
    for i in range(len(s1)):
        print()



# "00110"
# "00000" 2
# "00001" 3
# "00011"
# "00111"
# "01111"
# "11111"



# brute force

def way1(s):


    t = ["0"] * len(s)
    size = len(s)
    i = size - 1
    minCount = 99999
    while i >=0:
        count = 0
        for j in range(size-1,-1,-1):
            if t[j] != s[j]:
                count += 1
        minCount = min(minCount, count)
        t[i] = "1"
        i -= 1
        # print(i)

    count = 0
    for j in range(size-1,-1,-1):
        if t[j] != s[j]:
            count += 1
    minCount = min(minCount, count)

    return minCount


# s

def way2(s):

    zero , one = s.count("0"), 0
    output = zero
    for d in s:
        if d=='0':
            zero -= 1
        if d == '1':
            one += 1
        output = min (output, zero+one)


    return output


def way3(s) :
    ones = 0
    flips = 0

    for c in s:
        if(c == "0"):
            if(ones == 0):
                continue

            flips += 1
        else:
            ones += 1

        if(flips > ones):
            flips = ones

    return flips

s = "00110"
s = "010110"
# s = "00011000"
print(way3(s))
