
def way1(height):
    max_left = [0]
    max_right = [0]
    max_ll = height[0]
    for i in range(1,len(height)):
        max_left.append(max_ll)
        max_ll = max(max_ll, height[i])




    max_rr = height[-1]
    for i in range(len(height)-1,0,-1):
        max_rr = max(max_rr, height[i])
        max_right.append(max_rr)

    max_right.reverse()
    print("heght",height)
    print("left",max_left)
    print("right",max_right)
    count = 0
    for i in range(1,len(height)-1):
        least = min(max_right[i], max_left[i])
        part = least - height[i]
        if part > 0:
            count += part

    return count


    print(height)
    print(max_left)
    print(max_right)



height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]

print(way1(height))