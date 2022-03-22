

class MyNode:
    def __init__(self,next,val) -> None:
        self.next = next
        self.data = val


def MaximumPagesV2(head:MyNode):

    '''
    1 -> 4 -> 3 -> 2
    1 <- 4 3->2
    leftHead = None
    rightHead = 2


    '''
    leftHead = None
    rightHead = None

    fast = head
    slow = head
    counter = 0
    while fast != None:
        leftHead = slow
        slow = slow.next
        fast = fast.next.next
        counter+=1

    rightHead= slow

    next = None
    while counter  > 0:
        tmp = head
        head = head.next
        tmp.next = next
        next = tmp
        counter -=1


    leftHead = next



    maxVal = 0
    while leftHead and rightHead:
        maxVal = max(maxVal,leftHead.data+rightHead.data)
        leftHead = leftHead.next
        rightHead = rightHead.next

    return maxVal



def my_way(head):

    count = 0
    fast = head
    slow = head

    leftHead = rightHead = None

    # while fast != None:
    #     leftHead = slow
    #     slow = slow.next
    #     fast = fast.next.next
    #     count += 1

    while fast != None :
        leftHead = slow
        slow = slow.next
        fast = fast.next.next
        count += 1

    rightHead = slow

    next = None

    while count > 0:
        tmp = head
        head = head.next
        tmp.next = next
        count -= 1

    leftHead = next

    maxVal = 0
    while leftHead and rightHead:
        maxVal = max(maxVal, leftHead.data + rightHead.data)

    return maxVal








if __name__ == '__main__':

    node6 = MyNode(None,1)
    node5 = MyNode(node6,4)
    node4 = MyNode(node5,5)
    node3 = MyNode(node4,6)
    node2 = MyNode(node3,3)
    node1 = MyNode(node2,8)

    # res = MaximumPagesV2(node1)
    res = my_way(node1)
    print(res)

