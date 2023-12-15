class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.min_val = float('inf')
        self.left = None
        self.right = None

def build_segment_tree(nums, start, end):
    if start > end:
        return None

    root = SegmentTreeNode(start, end)

    if start == end:
        root.min_val = nums[start]
    else:
        mid = (start + end) // 2
        root.left = build_segment_tree(nums, start, mid)
        root.right = build_segment_tree(nums, mid + 1, end)
        root.min_val = min(root.left.min_val, root.right.min_val)

    return root

def query_segment_tree(root, start, end):
    if not root or end < root.start or start > root.end:
        return float('inf')

    if start <= root.start and end >= root.end:
        return root.min_val

    mid = (root.start + root.end) // 2
    return min(query_segment_tree(root.left, start, min(mid, end)),
               query_segment_tree(root.right, max(mid + 1, start), end))

nums = [2, 5, 1, 4, 9, 3]
root = build_segment_tree(nums, 0, len(nums) - 1)

result1 = query_segment_tree(root, 1, 4)
print(result1) 

result2 = query_segment_tree(root, 2, 5)
print(result2) 

result3 = query_segment_tree(root, 0, 3)
print(result3)  
