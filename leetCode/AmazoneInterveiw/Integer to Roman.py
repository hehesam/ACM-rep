def intToRoman(num: int) -> str:
    dic = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    lst = [x for x in dic]
    res = []
    for i in range(len(lst)-1,-1,-1):
        if num >= lst[i]:
            val = num//lst[i]
            roman = dic[lst[i]] * val
            res.append(roman)
            num%=lst[i]

    return ''.join(res)


num = 3

print(intToRoman(num))