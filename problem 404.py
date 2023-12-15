class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

def build_segment_tree(nums, start, end):
    if start > end:
        return None

    root = SegmentTreeNode(start, end)

    if start == end:
        root.total = nums[start]
    else:
        mid = (start + end) // 2
        root.left = build_segment_tree(nums, start, mid)
        root.right = build_segment_tree(nums, mid + 1, end)
        root.total = root.left.total + root.right.total

    return root

def update_segment_tree(root, index, val):
    if root.start == root.end == index:
        root.total = val
        return

    mid = (root.start + root.end) // 2
    if index <= mid:
        update_segment_tree(root.left, index, val)
    else:
        update_segment_tree(root.right, index, val)

    root.total = root.left.total + root.right.total

def query_segment_tree(root, start, end):
    if not root or end < root.start or start > root.end:
        return 0

    if start <= root.start and end >= root.end:
        return root.total

    mid = (root.start + root.end) // 2
    return query_segment_tree(root.left, start, min(mid, end)) + query_segment_tree(root.right, max(mid + 1, start), end)

def count_range_sum(nums, lower, upper):
    def count_recursive(root, val):
        if not root:
            return 0

        count = 0
        if val + root.total <= upper and val + root.total >= lower:
            count += 1

        count += count_recursive(root.left, val)
        count += count_recursive(root.right, val)

        return count

    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    root = build_segment_tree(prefix_sum, 0, len(prefix_sum) - 1)
    result = 0

    for i in range(len(nums)):
        result += count_recursive(root, prefix_sum[i] - lower) - count_recursive(root, prefix_sum[i] - upper - 1)
        update_segment_tree(root, i + 1, prefix_sum[i + 1])

    return result

nums = [-2, 5, -1]
lower = -2
upper = 2
result = count_range_sum(nums, lower, upper)
print(result)  
