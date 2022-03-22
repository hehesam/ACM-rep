def way1(nums):

    nums.sort()
    sub_num = []
    sum = 0
    for i in range(len(nums)):
        for j in range(i):
            sum += abs(nums[j]-nums[i])
            sub_num.append(nums[j:i])
            print(sum, sub_num)

    return sum



nums = [1,2,3]
# nums = [1,3,3]
# nums = [4,-2,-3,4,1]
print(abs(nums[0]-nums[0]))

print(way1(nums))










nums = [1,2,3]