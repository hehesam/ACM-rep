class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_travelsal(root, arr, i):
    if i<len(arr) and arr[i] != None:
        root =  Node(arr[i])
        root.left = level_order_travelsal(root.left, arr, 2*i+1)
        root.right = level_order_travelsal(root.right, arr, 2*i+2)
        return root




def BFS(root):
        print(root.val)
        if root.left:
            BFS(root.left)
        if root.right:
            BFS(root.right)

def max_path_sum(root, max_path):
    if root == None:
        return 0
    left_sum = max_path_sum(root.left, max_path)
    right_sum = max_path_sum(root.right, max_path)

    current_sum = root.val + left_sum + right_sum

    if current_sum>max_path[0]:
        max_path.pop()
        max_path.append(current_sum)

    return root.val + max(left_sum, right_sum)


arr = [-10,9,20,None,None,15,7]
root = level_order_travelsal(None, arr, 0)

# BFS(root)
max_path = [-999]

max_path_sum(root, max_path)
print(max_path)