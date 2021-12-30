class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None



def tree_includes(root, trg):
    if root == None:
        return False
    if root.val == trg:
        return True
    return tree_includes(root.left, trg) or tree_includes(root.right, trg)

def tree_includes2(root, trg):
    if root == None :
        return False

    que = []
    que.append(root)
    while len(que):
        current = que.pop(0)
        if current.val == trg:
            return True
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h



print(tree_includes(None, "f")) # -> True
print(tree_includes2(None, "f"))
