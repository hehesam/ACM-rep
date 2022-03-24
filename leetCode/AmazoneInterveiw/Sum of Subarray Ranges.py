


def way1(nums):

    res = 0

    for i in range(2,len(nums)+1):
        for j in range(0,(len(nums)-i+1)):
            ran = nums[j:j+i]
            res += max(ran)-min(ran)
    return res

def way2(nums):
    # nums.sort()
    res = 0
    n = len(nums)
    for i in range(n):
        l,r = nums[i],nums[i]
        for j in range(i,n):
            l = min(l, nums[j])
            r = max(r,nums[j])
            res += r-l
            print(l,r, res)

    return res


def way3(nums):
    res = 0
    inf = float('inf')
    nums1 = [-inf] + nums + [-inf]
    s = []
    for i, x in enumerate(nums1):
        while s and nums1[s[-1]] > x:
            j = s.pop()
            k = s[-1]
            res -= nums1[j] * (i - j) * (j - k)
        s.append(i)

    nums2 = [inf] + nums + [inf]
    s = []
    for i, x in enumerate(nums2):
        while s and nums2[s[-1]] < x:
            j = s.pop()
            k = s[-1]
            res += nums2[j] * (i - j) * (j - k)
        s.append(i)
    return res


# def way4(nums):
#     l,r = 0,0
#     while l <
nums = [1,2,3]
nums = [1,3,3]
nums = [-1,3,4,4]
#
nums = [4,-2,-3,4,1]
# print(abs(nums[0]-nums[0]))

print(way3(nums))




nums = [1,2,3]