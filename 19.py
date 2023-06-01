"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
I take the do it in one round path:
1. When you try to find n'th node from the end of the list, we can do it by using 2 pointer
    "p" pointer which try to goes trough all the node in the Linked list
    "q" pointer which is the n'th previous node of p

2. When "p" pointer reach the end of Linked list, "q" pointer is the Node that is n'th node from the end of Linked list
Which mean q is the node we need to remove

3. A link list removed will have quite some cases need to be cover:
    1. The removed node is at beginning of the Linked list, the head node:
        - Quick one: If there is only one Node in the link list, and n == 1
        - Other case:
            Set up a previous node of "q" pointer (the node we need to remove); let call it "pre" pointer
            If "pre" isn't defined, that mean "q" pointer is the "head"
        - Handle:
            head = head.next
            free(q)
            return head
    2. Other case:
        - Handle
            pre.next = q.next
            free(q)
            return head
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cover quick case
        if n == 1 and head.next == None:
            return None
        
        # Step 1: set up 'p' and 'q' pointer
        p = head
        for i in range(n):
            p = p.next
        q = head

        # Step 2: loop through all the Linked list with 'p', while mantainning and 'q' pointer
        # is the n'th node before 'p'
        # Also traceback 'pre' pointer, which i the previous node of 'q' 
        pre = None
        while p:
            p = p.next
            pre = q
            q = q.next


        # Step 3: Handle node removing

        # Case 2: This is when head != q
        if pre != None:
            # pre.next = p.next
            pre.next = pre.next.next
            # free(q) 
            return head
        
        # Case 1: This is when head == q
        # head = head.next or head = q.next
        # free(q)
        return q.next
    

"""
# Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
# Example 2:

Input: head = [1], n = 1
Output: []
# Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

# Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz"""