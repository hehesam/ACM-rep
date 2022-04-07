
import time
import random
import math

def printer(dp):

    for i in dp:
        print(i)

def DP(nums):
    mat = [[0 for i in range(len(nums))] for j in range(len(nums))]
    max = 0
    for i in range(len(nums)):
        for j in range(i , len(nums)):
            if j > 0:
                mat[i][j] = mat[i][j-1] + nums[j]
            else:
                mat[i][j] = nums[j]
            if mat[i][j] > max:
                max = mat[i][j]
            printer(mat)
            print('\n\n')
            time.sleep(1)

    return max


def REC(nums, j, val, max):
    if j == len(nums):
        return max
    val += nums[j]
    if val > max:
        max = val
    return REC(nums, j+1, val, max)





def DP2(nums):
    max = -999
    ss1 = time.time()
    for i in range(len(nums)):
        ss2 = time.time()
        buff = 0
        flag = False
        for j in range(i,len(nums)):
            if not flag:
                buff = nums[j]
                flag = True
            else :

                buff = buff + nums[j]

            if buff > max:
                max = buff
    print("for loop time : ", time.time()-ss1)

    ss2 = time.time()
    max1 = max
    max = -999

    i = 0
    while i < (len(nums)):
        buff = 0
        flag = False

        for j in range(i, len(nums)):
            if not flag:
                buff = nums[j]
                flag = True
            else :

                buff = buff + nums[j]

            if buff > max:
                max = buff
        # print("inner loop time : ", time.time()-ss2)
        i+=1

    print('while loop time : ', time.time()-ss2)
    max2 = max
    return max1,max2


def DP3(nums):
    curr =  max1 = nums[0]

    for num in nums[1:]:
        curr = max(num, curr+num)
        max1 = max(max1, curr)

    return max1





def DP4(nums):
    mm = curr = nums[0]

    for num in nums[1::]:
        curr = max(num, curr+num)
        mm = max(mm , curr)
    return mm

#
# def maxSubArray(nums, left , right):
#     if left > right :
#         return 0
#     mid = (left + right) //2
#
#     curr = best_left_sum = best_right_sum = 0
#
#
#     for i in range(mid-1, left-1, -1):
#     # for i in range(left, mid-1):
#         curr += nums[i]
#         best_left_sum = max(best_left_sum, curr)
#
#     curr = 0
#
#     for i in range(mid + 1, right+1):
#         curr += nums[i]
#         best_right_sum = max(best_right_sum, curr)
#
#
#     best_combined_sum = nums[mid] + best_right_sum + best_left_sum
#
#     left_half = maxSubArray(nums, left, mid-1)
#     right_half = maxSubArray(nums, mid+1, right)
#
#
#     return max(best_combined_sum, left_half, right_half)




def maxSubArray(nums, left, right):
    # Base case - empty array.
    if left > right:
        return -999

    mid = (left + right) // 2
    curr = best_left_sum = best_right_sum = 0

    # Iterate from the middle to the beginning.
    for i in range(mid - 1, left - 1, -1):
        curr += nums[i]
        best_left_sum = max(best_left_sum, curr)

    # Reset curr and iterate from the middle to the end.
    curr = 0
    for i in range(mid + 1, right + 1):
        curr += nums[i]
        best_right_sum = max(best_right_sum, curr)

    # The best_combined_sum uses the middle element and
    # the best possible sum from each half.
    best_combined_sum = nums[mid] + best_left_sum + best_right_sum

    # Find the best subarray possible from both halves.
    left_half = maxSubArray(nums, left, mid - 1)
    right_half = maxSubArray(nums, mid + 1, right)

    # The largest of the 3 is the answer for any given input array.
    return max(best_combined_sum, left_half, right_half)

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-1]


# nums = [1, -3]
# nums = [5,4,-1,7,8]
# nums = [random.randrange(-99,99) for i in range(99999)]


# print(nums)
print(DP(nums))
# max = 0
# for i in range(len(nums)):
#     res = REC(nums, i , 0, max)
#     if res > max:
#         max = res
#
# print(max)
# print(DP2(nums))

# print(DP3(nums))

print(maxSubArray(nums,0, len(nums)-1 ))
