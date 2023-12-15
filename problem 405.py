class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = None
        self.right = None

def build_segment_tree(nums, start, end):
    if start > end:
        return None

    root = SegmentTreeNode(start, end)

    if start == end:
        root.count = 0
    else:
        mid = (start + end) // 2
        root.left = build_segment_tree(nums, start, mid)
        root.right = build_segment_tree(nums, mid + 1, end)

    return root

def update_segment_tree(root, index, val):
    if root.start == root.end == index:
        root.count += 1
        return

    mid = (root.start + root.end) // 2
    if index <= mid:
        update_segment_tree(root.left, index, val)
    else:
        update_segment_tree(root.right, index, val)

    root.count = root.left.count + root.right.count

def query_segment_tree(root, start, end):
    if not root or end < root.start or start > root.end:
        return 0

    if start <= root.start and end >= root.end:
        return root.count

    mid = (root.start + root.end) // 2
    return query_segment_tree(root.left, start, end) + query_segment_tree(root.right, start, end)

def count_smaller(nums):
    result = []
    max_val = max(nums)
    min_val = min(nums)
    root = build_segment_tree(nums, min_val, max_val)

    for num in reversed(nums):
        result.append(query_segment_tree(root, min_val, num - 1))
        update_segment_tree(root, num, 1)

    return result[::-1]

nums = [5, 2, 6, 1]
result = count_smaller(nums)
print(result)  
