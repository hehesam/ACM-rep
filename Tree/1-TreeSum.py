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
def tree_sum2(root):
    qu = []
    qu.append(root)
    sum = 0
    while len(qu):
        current = qu.pop(0)
        sum+=current.val
        if current.left:
            qu.append(current.left)
        if current.right:
            qu.append(current.right)
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

print(tree_sum(a)) # -> 21
print(tree_sum2(a))
