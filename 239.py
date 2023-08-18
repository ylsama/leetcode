from typing import List


class Heap:
    def getChild(self, x):
        res = []
        if x*2+1 <= self.size:
            res.append(x*2+1)
        if x*2 <= self.size:
            res.append(x*2)
        return res

    def getParrent(x):
        return x // 2

    def __init__(self, arr):
        self.heap = [-1] + arr
        self.size = len(arr)
        self.pos = list(range(self.size + 1))
        self.revertPos = list(range(self.size + 1))
        self.next = 1

        for i in range(1, self.size+1):
            self.update(i)

        for i in range(1, self.size+1):
            self.revertPos[self.pos[i]] = i

    def update(self, x):
        if x == 1:
            return
        px = Heap.getParrent(x)
        if self.heap[x] > self.heap[px]:
            self.heap[x], self.heap[px] = self.heap[px], self.heap[x]
            self.pos[x], self.pos[px] = self.pos[px], self.pos[x]
            self.revertPos[self.pos[x]], self.revertPos[self.pos[px]
                                                        ] = self.revertPos[self.pos[px]], self.revertPos[self.pos[x]]

            self.update(px)

    def downgrade(self, x):
        cx_arr = self.getChild(x)
        if len(cx_arr) == 2 and self.heap[cx_arr[1]] > self.heap[cx_arr[0]]:
            cx_arr.pop(0)
        for cx in cx_arr:
            if self.heap[x] < self.heap[cx]:
                self.heap[x], self.heap[cx] = self.heap[cx], self.heap[x]
                self.pos[x], self.pos[cx] = self.pos[cx], self.pos[x]
                self.revertPos[self.pos[x]], self.revertPos[self.pos[cx]
                                                            ] = self.revertPos[self.pos[cx]], self.revertPos[self.pos[x]]
                self.downgrade(cx)
                break

    def incNext(self):
        if self.next >= self.size:
            self.next = 1
        else:
            self.next += 1

    def replace(self, v):
        pos = self.revertPos[self.next]
        self.incNext()
        old = self.heap[pos]
        self.heap[pos] = v
        if old < v:
            self.update(pos)
        else:
            self.downgrade(pos)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = Heap(nums[:k])
        res = [heap.heap[1]]

        for i in nums[k:]:
            heap.replace(i)
            res.append(heap.heap[1])

        return res


def main():
    a = Solution()
    res = a.maxSlidingWindow([1, 9, 8, 4, 4, 3, 2, 5, 1, 3, -1, -3, 5, 3, 6, 7, 1, 3, -1, -3, 5, 3, 6, 7, 1, 3, -1, -3, 5, 3, 6, 7],
                             8)
    print(res)


if __name__ == "__main__":
    main()
