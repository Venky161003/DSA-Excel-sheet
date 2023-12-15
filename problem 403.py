class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)
        self.mod = 10**9 + 7

    def update(self, index, value):
        index += self.size
        self.tree[index] += value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def query(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

class Solution:
    def createSortedArray(self, instructions):
        max_val = max(instructions)
        segment_tree = SegmentTree(max_val + 1)
        total_cost = 0

        for i, num in enumerate(instructions):
            less_than_count = segment_tree.query(0, num - 1)
            greater_than_count = i - segment_tree.query(num + 1, max_val)
            total_cost += min(less_than_count, greater_than_count)
            segment_tree.update(num, 1)

        return total_cost % segment_tree.mod

instructions = [1, 5, 6, 2]
solution = Solution()
result = solution.createSortedArray(instructions)
print(result)  
