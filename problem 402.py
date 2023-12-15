class SegmentTreeNode:
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build_segment_tree(nums, 0, len(nums) - 1)

    def build_segment_tree(self, nums, start, end):
        if start > end:
            return None

        root = SegmentTreeNode(start, end)

        if start == end:
            root.val = nums[start]
        else:
            mid = (start + end) // 2
            root.left = self.build_segment_tree(nums, start, mid)
            root.right = self.build_segment_tree(nums, mid + 1, end)
            root.val = root.left.val + root.right.val

        return root

    def update(self, index, val):
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if not root:
            return

        if root.start == root.end == index:
            root.val = val
            return

        mid = (root.start + root.end) // 2
        if index <= mid:
            self.update_helper(root.left, index, val)
        else:
            self.update_helper(root.right, index, val)

        root.val = root.left.val + root.right.val

    def sumRange(self, left, right):
        return self.sumRange_helper(self.root, left, right)

    def sumRange_helper(self, root, left, right):
        if not root or right < root.start or left > root.end:
            return 0

        if left <= root.start and right >= root.end:
            return root.val

        mid = (root.start + root.end) // 2
        return self.sumRange_helper(root.left, left, min(mid, right)) + \
               self.sumRange_helper(root.right, max(mid + 1, left), right)

nums = [1, 3, 5]
num_array = NumArray(nums)

result1 = num_array.sumRange(0, 2)
print(result1)  

num_array.update(1, 2)

result2 = num_array.sumRange(0, 2)
print(result2) 
