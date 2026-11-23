class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)

        # visited = defaultdict(int)
        # res = 1
        # for i, e in enumerate(nums):
        #     tot = 0
        #     if e - 1 in store:
        #         visited[e]+=1
        #         tot = visited[e-1] + visited[e]
        #     res = max(res, tot)
        
        # return res

        if not nums:
            return 0

        res = 1
        for i, e in enumerate(nums):
            if e - 1 in store:
                continue
            print(e)
            tot = 1
            curr = e + 1
            while curr in store:
                tot += 1
                curr += 1
            res = max(tot,res)
        return res
            