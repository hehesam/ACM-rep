def way1(nums):
    prefix = [1]
    suffix = [1]

    for i in range(1,len(nums)):
        prefix.append(nums[i-1]*prefix[-1])

    for i in range(len(nums)-2, -1, -1):
        print(nums[i])
        suffix.append(nums[i+1]*suffix[-1])

    suffix.reverse()
    print(prefix)
    print(suffix)


nums = [1,2,3,4]
print(way1(nums))