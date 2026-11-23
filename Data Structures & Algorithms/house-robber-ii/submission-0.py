class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            one, two = 0, 0
            for i in nums:
                one, two = two,max(one + i, two)
            return two
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))