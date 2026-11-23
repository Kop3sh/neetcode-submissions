class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        counts = defaultdict(int)
        prd = 1
        for i in nums:
            counts[i] += 1
            if i != 0:
                prd *= i

        if counts[0] > 1:
            return res
        
        # print(n)
        for i in range(n):
            # print(i, nums[i])
            if counts[0] == 1 and nums[i] != 0:
                continue
            if counts[0] == 1 and nums[i] == 0:
                res[i] = prd
                break
            res[i] = prd // nums[i]

        return res




        