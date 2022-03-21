class MyNode:
    def init(self,next,val) -> None:
        self.next = next
        self.val = val

max_val = -1
def helper(slow,fast):
        slow = slow.next
        fast = fast.next.next

        if fast and fast.next:
            ret = helper(slow,fast)
            max_val = max(max_val,ret.val+slow.val)
            return ret.next
        else:
            return slow.next

def MaximumPages(head:MyNode):

    slow = head
    fast = head

    max_val = 1000


    helper(head,head)
    return max_val






if name == 'main':

    node4 = MyNode(None, 2 )
    node3 = MyNode(node4,3)
    node2 = MyNode(node3,4)
    node1 = MyNode(node2,1)

    res = MaximumPages(node1)
    print(res)