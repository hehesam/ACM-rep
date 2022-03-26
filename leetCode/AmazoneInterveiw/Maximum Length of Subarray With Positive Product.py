





# brute force works for 111/112 test cases

def way1(nums):
    max_num = 0
    size = len(nums)
    if size==1:
        if nums[0] > 0:
            return 1


    i = 0
    while i < size:
    # for i in range(size):
        # for large inputs
        if size-1 <= max_num:
            return max_num

        if nums[i] != 0:

            pos = neg = 0

            if nums[i] < 0:
                neg = 1
            else :
                pos = 1

            max_num = max(max_num, pos)

            # for j in range(i+1, size):
            j = i+1
            while j < size:
                if nums[j] < 0:
                    neg += 1
                elif nums[j] == 0:
                    break
                if neg %2 == 0:
                    max_num = max(max_num, j-i+1)
                j += 1
        i += 1
    return max_num





    # The idea is to keep track of the maximum length of subarray with negative product and maximum length of subarray with positive product, because depending on the sign of each number we encounter, we want to use each length to inform the other.
    # (1) pos[i] = maximum subarray length with positive product including nums[i] so far
    # (2) neg[i] = maximum subarray length with negative product including nums[i] so far
    # Here are the different possible cases:
    #   - If the number is negative:

    #       - If there is a non-empty subarray with negative product to the immediate left of this number:
    #           - Add this number to the subarray with positive product, since negative times negative equals positive.
    #       - Otherwise:
    #           - No subarray with positive product at this point.

    #       - If there is a non-empty subarray with positive product to the immediate left of this number:
    #           - Add this number to subarray with negative product, since positive times negative equals negative.
    #       - Otherwise:
    #           - Begin a new subarray with negative product, since a single negative value has a negative product.

    #   - If the number is positive:

    #       - If there is a non-empty subarray with positive product to the immediate left of this number:
    #           - Add this number to the subarray with positive product, since positive times positive equals positive.
    #       - Otherwise:
    #           - Begin a new subarray with positive product, since a single positive value has a positive product.

    #       - If there is a non-empty subarray with negative product to the immediate left of this number:
    #           - Add this number to subarray with negative product, since negative times positive equals negative.
    #       - Otherwise:
    #           - No array with negative product at this point.

def way2(nums):

    n = len(nums)
    pos = [0] * n
    neg = [0] * n

    if nums[0] < 0:
        neg[0] = 1
    if nums[0] > 0:
        pos[0] = 1

    for i in range(1,n):
        if nums[i] < 0:
            if neg[i-1] != 0:
                pos[i] = 1 + neg[i-1]
            if  pos[i-1] != 0:
                neg[i] = 1 + pos[i-1]
            else :
                neg[i] = 1
        elif nums[i] > 0:
            if pos[i-1] != 0:
                pos[i] = 1 + pos[i-1]
            else:
                pos[i] = 1

            if  neg[i-1] != 0:
                neg[i] = 1 + neg[i-1]
    return  max(pos)

nums = [1,-2,-3,4]
nums = [0,1,-2,-3,-4]

nums = [-1,-2,-3,0,1]

print(way2(nums))
