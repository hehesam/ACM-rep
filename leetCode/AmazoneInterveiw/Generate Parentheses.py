


def valid(A= "((()))"):
    bal = 0
    for c in A:
        print(c, bal)
        if c == '(': bal += 1
        else: bal -= 1
        if bal < 0: return False
    return bal == 0

print(valid())

#
#
#
# def generate(A, n, ans):
#     if len(A) == 2*n:
#         if valid(A):
#             ans.append("".join(A))
#     else:
#         A.append('(')
#         generate(A,n ,ans)
#         A.pop()
#         A.append(')')
#         generate(A, n, ans)
#         A.pop()
#
#
# n = 3
# ans = []
# A = []
# generate(A, n, ans)
# print(ans)