class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def level_order(arr, root, i, size):

    if i<size and arr[i] != None:
        temp = Node(arr[i])
        root = temp
        root.left = level_order(arr, root.left, 2*i+1, size)
        root.right = level_order(arr, root.right, 2*i+2, size)

    return root





def max_path_sum(root, max_sum):
    if root == None :
        return 0


    print(root.val)

    left_sum = max_path_sum(root.left, max_sum)
    right_sum = max_path_sum(root.right, max_sum)

    current_sum = root.val + left_sum + right_sum
    if current_sum > max_sum[0]:
        max_sum.pop(0)
        max_sum.append(current_sum)

    return root.val + max(left_sum, right_sum)




levelOrder = [1,2,3]

root = level_order(levelOrder, None, 0, len(levelOrder))
max_sum = [-999]
print(max_path_sum(root, max_sum))

print(max_sum)