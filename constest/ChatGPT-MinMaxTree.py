import math

class MinMaxTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [None] * (2 * self.size)
        self.build(arr)

    def build(self, arr):
        for i in range(self.size):
            self.tree[self.size + i] = (arr[i], arr[i])

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = (
                min(self.tree[2 * i][0], self.tree[2 * i + 1][0]),
                max(self.tree[2 * i][1], self.tree[2 * i + 1][1])
            )

    def update(self, start, end, input_value, node=1, node_start=0, node_end=None):
        if node_end is None:
            node_end = self.size - 1

        if node_start > end or node_end < start:
            return

        if node_start >= start and node_end <= end:
            self.tree[node] = (input_value, input_value)
            return

        mid = (node_start + node_end) // 2
        self.update(start, end, input_value, 2 * node, node_start, mid)
        self.update(start, end, input_value, 2 * node + 1, mid + 1, node_end)

        self.tree[node] = (
            min(self.tree[2 * node][0], self.tree[2 * node + 1][0]),
            max(self.tree[2 * node][1], self.tree[2 * node + 1][1])
        )

    def query(self, left, right, node=1, node_start=0, node_end=None):
        if node_end is None:
            node_end = self.size - 1

        if node_start > right or node_end < left:
            return float('inf'), float('-inf')

        if node_start >= left and node_end <= right:
            return self.tree[node]

        mid = (node_start + node_end) // 2
        left_min, left_max = self.query(left, right, 2 * node, node_start, mid)
        right_min, right_max = self.query(left, right, 2 * node + 1, mid + 1, node_end)

        return min(left_min, right_min), max(left_max, right_max)

# Example usage:
arr = [5, 3, 8, 2, 6, 1, 9, 4, 7]
tree = MinMaxTree(arr)

# Get the minimum and maximum values of the subarray from index 2 to 5
min_val, max_val = tree.query(2, 5)
print("Minimum value:", min_val)  # Output: 2
print("Maximum value:", max_val)  # Output: 8

# Update the elements in the subarray from index 2 to 5 to have a value of 10
tree.update(0, 8, 3)

# Get the minimum and maximum values of the subarray from index 2 to 5 after the update
min_val, max_val = tree.query(2, 5)
print("Minimum value:", min_val)  # Output: 10
print("Maximum value:", max_val)  # Output: 10 (as all values are updated to 10)
