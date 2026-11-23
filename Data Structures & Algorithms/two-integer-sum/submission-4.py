class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in rems:
                return [rems[r], i]
            rems[n] = i