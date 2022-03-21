def way1(weight):
    n = len(weight)
    ans = 0
    for i in range(n):
        mx = weight[i]
        mn = weight[i]
        for j in range(i+1, n):
            mx = max(mx, weight[j])
            mn = min(mn, weight[j])

            ans += (mx-mn)
    return ans



def fill_cgl_cgr(n, A, conf):
    st = []
    for i in range(n):
        while   len(st)!=0 and
aa = [1,2,3]

print(way1(aa))