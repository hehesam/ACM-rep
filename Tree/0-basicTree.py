class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def depth_first_value_1(root):
    if root == None:
        return None
    stack = []
    arr = []
    stack.append(root)
    while len(stack):
        current = stack.pop()
        print(current.val)
        arr.append(current.val)

        if (current.right):
            stack.append(current.right)
        if(current.left):
            stack.append(current.left)

    return arr

def depth_first_value_2(root):
    if root == None:
        return []
    leftStack = depth_first_value_2(root.left)
    rightStack = depth_first_value_2(root.right)
    res = [root.val]
    return res+leftStack+rightStack


def breth_first_value_1(root):
    if root:
        que = []
        res = []
        que.append(root)
        while len(que):
            current = que.pop(0)
            print(current.val)
            res.append(current.val)
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)

        return res

def breth_first_value_2(que,res):
    if len(que):
        current = que.pop(0)
        res.append(current.val)
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)

        breth_first_value_2(que, res)
    return res


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
# print(depth_first_value1(a))
# print(depth_first_value_2(a))
print(breth_first_value_1(a))
print(breth_first_value_2([a],[]))

