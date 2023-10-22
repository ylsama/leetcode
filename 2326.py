from typing import List, Optional
# Definition for singly-linked list.
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
        p = p.next
        k -= 1
    return listR

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for i in range(n)] for i in range(m)]
        x, y, dx, dy = 0, 0, 0 , 1
        p = head
        while p:
            value = p.val
            p = p.next
            result[x][y] = value
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and  0 <= ny < n:
                if result[nx][ny] == -1:
                    x, y = nx, ny
                    continue
            
            if dx == 0:
                dx, dy = dy, 0
            else:
                dx, dy = 0, 0 - dx
            nx, ny = x + dx, y + dy
            x, y = nx, ny
        return result

if __name__=="__main__":
    a = Solution()
    result = a.spiralMatrix(m = 3, n = 5, head = create([3,0,2,6,8,1,7,9,4,2,5,5,0]))
    for i in result:
        print(i)