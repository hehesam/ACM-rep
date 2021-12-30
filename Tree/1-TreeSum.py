class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_sum(root):
    if root == None:
        return 0
    sum = root.val
    sum+=tree_sum(root.right)
    sum+=tree_sum(root.left)
    return sum


a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

print(tree_sum(None)) # -> 21
