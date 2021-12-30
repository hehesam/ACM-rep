class Node:
    def __init__(self, val):
        self.val  = val
        self.right = None
        self.left = None

def tree_min_value(root):
    if root == None:
        return False
    que = []
    que.append(root)
    min = 999
    while len(que):
        current = que.pop(0)
        if current.val < min:
            min = current.val
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return min

def tree_min_value2(root):

    if root ==  None:
        return 999

    return min(root.val, tree_min_value2(root.left), tree_min_value2(root.right))


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

print(tree_min_value(a)) # -> -2
print(tree_min_value2(a))
