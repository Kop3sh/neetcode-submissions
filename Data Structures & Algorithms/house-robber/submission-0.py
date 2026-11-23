class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i, total):
        #     if i < n:
        #         return total

        #     return max(total, dfs(i+2, total + nums[i]))
        
        # return max(dfs(0, 0), dfs(1, 0))
        one, two = 0, 0
        # [one, two, i, i + 1, ...]
        for i in nums:
            one, two = two, max(one + i, two)
        return two