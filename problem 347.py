def rob(nums):
    if not nums:
        return 0

    n = len(nums)

    if n == 1:
        return nums[0]

    def rob_range(start, end):
        dp = [0] * n
        dp[start] = nums[start]
        dp[start + 1] = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[end]

    result1 = rob_range(0, n - 2)

    result2 = rob_range(1, n - 1)

    return max(result1, result2)

nums = [2, 3, 2]
result = rob(nums)
print(result) 
