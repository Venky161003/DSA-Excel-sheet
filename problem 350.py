def canJump(nums):
    max_reach = 0

    for i, num in enumerate(nums):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + num)

        if max_reach >= len(nums) - 1:
            return True

    return False

nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

result1 = canJump(nums1)
result2 = canJump(nums2)

print(result1) 
print(result2) 
