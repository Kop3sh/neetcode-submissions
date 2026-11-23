class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, n in enumerate(nums):
            d = target - n
            diff[d] = i
        
        for i, n in enumerate(nums):
            if n in diff and i != diff[n]:
                return [i, diff[n]]
        