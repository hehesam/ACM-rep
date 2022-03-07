

def decoder(s, numbers):
    stack = []
    for i in range(len(s)):
        if s[i] == ']':
            decodeString = ""
            while(stack[-1] != '['):
                decodeString += stack.pop()
            stack.pop()
            base = 1
            k = 0
            while len(stack) and stack[-1] in numbers:
                k = k+ numbers[stack.pop()]*base
                base *= 10

            while k :
                for j in range(len(decodeString)-1,-1,-1):
                    stack.append(decodeString[j])
                k -= 1

        else :
            stack.append(s[i])

    res = ""
    stack.reverse()
    while len(stack):
        res += stack.pop()


    return res


def decoder2(s, numbers):
    stack = []
    for i in range(len(s)):
        if s[i] == ']':
            partString = ""
            while stack[-1] != '[':
                partString += stack.pop()

            stack.pop()
            base = 1
            k = 0

            while len(stack) and stack[-1] in numbers:
                k += numbers[stack.pop()]*base
                base *= 10

            while k :
                for j in range(len(partString)-1, -1, -1):
                    stack.append(partString[j])
                k -= 1
        else:
            stack.append(s[i])

    res = ""
    for i in stack:
        res += i
    return  res

def decoder3(s: str) -> str:
    if not s:
        return ""

    countStack = []
    stringStack = []

    counter = 0
    curStr = ""
    for ch in s:
        if ch.isdigit():
            counter = counter * 10 + int(ch)
        elif ch == "[":
            countStack.append(counter)
            stringStack.append(curStr)

            counter = 0
            curStr = ""
        elif ch == "]":

            counter = countStack.pop()
            tmpstr = stringStack.pop()

            tmpstr += curStr * counter
            curStr = tmpstr
            counter = 0
        else:
            curStr += ch
    return curStr

def decoder4(s: str) -> str:
    stack = []
    i = 0

    while i < len(s):
        if s[i] != "]":
            stack.append(s[i])

        else:
            tmp = ""
            num = ""

            while stack[-1] != "[":
                tmp += stack.pop()

            stack.pop()

            while stack and stack[-1].isdigit():
                num += stack.pop()

            tmp = tmp[::-1] * int(num[::-1])

            for t in tmp:
                stack.append(t)

        i += 1

    return "".join(stack)


# s = "3[a2[c]]"

s = "3[a]2[bc]"

# s = "2[abc]3[cd]ef"
s  = "100[leetcode]"

numbers = {}
for i in range(1,301):
    numbers[str(i)] = i

print(decoder4(s))