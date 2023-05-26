from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 1
        p = head
        while p.next:
            n+=1
            p = p.next
        kh = head
        kr = head
        for i in range(1,k-1):
            kh = kh.next
        for i in range(1,n-k):
            kr = kr.next
        if k*2>n:
            tmp=kh
            kh=kr
            kr=tmp
        print(kh.val, kr.val)
        if k!=1 and k!=n:
            tmp = kh.next.next
            kh.next.next = kr.next.next
            kr.next.next = tmp
            tmp = kh.next
            kh.next = kr.next
            kr.next = tmp
        else:
            tmp = kh.next
            kh.next = kr.next.next
            kr.next.next = tmp
            head = kr.next
            kr.next = kh
        p = head
        while p:
            print(p.val)
            p = p.next
        
        # print (head, k)


a = Solution()
head = ListNode(1)
p = head
for i in [2,3,4,5,6]:
    p.next = ListNode(i)
    p = p.next

a.swapNodes(head,2)
