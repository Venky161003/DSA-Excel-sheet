class Solution:
	def singleNumber(self,nums):
	    set_ = set()
 
        n = len(nums)

        for i in nums:
            if i in set_:
                set_.remove(i)
            else:
                set_.add(i)
        return sorted(list(set_))
