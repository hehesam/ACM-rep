class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path_sum(root):
    if root.left == None and root.right == None:
        return root.val
    if root.left == None :
        return root.val + max_path_sum(root.right)
    if root.right == None:
        return root.val + max_path_sum(root.left)

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


def max_path_sum2(root):
    if root==None:
        return -999
    return root.val + max(max_path_sum2(root.left), max_path_sum2(root.right))


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

print(max_path_sum(a)) # -> 18
print(max_path_sum2(a))