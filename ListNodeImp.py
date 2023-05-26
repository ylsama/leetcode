
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
    return listR

head = create([1,2,3,4,5])
print(toList(head))

