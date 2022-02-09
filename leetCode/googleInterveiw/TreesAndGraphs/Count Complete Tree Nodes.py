class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def tree_maker(arr, parent ,index):
    if index < len(arr):
        parent = node(arr[index])
        # print(tmp.val)
        parent.left = tree_maker(arr,parent.left ,2*index+1)
        parent.right = tree_maker(arr,parent.right ,2*index+2)
        return parent


def tree_printer(root):
    if root:
        res = 1
        # print(root.val)
        if root.right !=  None:
            res += tree_printer(root.right)
        if root.left !=  None:
            res += tree_printer(root.left)
        return res
    else:
        return 0




root = [1]

res = tree_maker(root,None ,0)

print(tree_printer(res))



