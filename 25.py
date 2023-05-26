from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create(sample):
        head = ListNode(0)
        p = head
        for i in sample:
            p.next = ListNode(i)
            p=p.next
        return head.next

def toList(head, k=10):
    p = head
    listR =[]
    while p and k>0:
        listR += [p.val]
        p=p.next
        k-=1
    return listR

def swapH(head,k):
    head = ListNode(0,head)
    p = [head]
    for i in range(k):
        if p[i].next == None:
            return head.next
        p.append(p[i].next)
    # for i in p: 
        # print(i.val)
    p[0].next = p[k]
    p[1].next = p[k].next
    for i in range(2,k+1):
        p[i].next = p[i-1]
    p[1].next = swapH(p[1].next,k)
    return head.next 

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head = ListNode(0,head)
        p = [head]
        for i in range(k):
            if p[i].next == None:
                return head.next
            p.append(p[i].next)
        p[0].next = p[k]
        p[1].next = p[k].next
        for i in range(2,k+1):
            p[i].next = p[i-1]
        p[1].next = self.reverseKGroup(p[1].next,k)
        return head.next 
    
if __name__ == "__main__":
    head = create([1,2,3,4,5])
    print(toList(swapH(head,1)))

