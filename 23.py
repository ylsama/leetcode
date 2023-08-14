from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, list1: [Optional[ListNode]])  -> Optional[ListNode]:
        head = ListNode(0)
        p = head
        while list1 and list2:
            if list1.val <list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return head.next

a = Solution()
head = ListNode(1)
p = head
for i in [2,3,4,5,6]:
    p.next = ListNode(i)
    p = p.next

merge = a.merge(head, ListNode(3))
while merge:
    print(merge.val)
    merge = merge.next
