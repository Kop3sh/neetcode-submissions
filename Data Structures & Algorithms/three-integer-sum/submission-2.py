class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        res = set()

        nums.sort()
        idx = {}
        for i, v in enumerate(nums):
            idx[v] = i
        
        n = len(nums)
        print(nums)
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[i] + nums[j]
                if  (- diff) in idx and idx[-diff] != i and idx[-diff] != j and idx[-diff] > j:
                    # print(diff, -diff)
                    # res.append([nums[i], nums[j], -diff])
                    res.add(tuple([nums[i], nums[j], -diff]))

        # return res
        return [list(e) for e in res]
        