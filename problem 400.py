class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)

result1 = num_array.sumRange(0, 2)
print(result1)  
result2 = num_array.sumRange(2, 5)
print(result2)

result3 = num_array.sumRange(0, 5)
print(result3)  
