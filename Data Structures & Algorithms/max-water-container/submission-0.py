class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        h2i = defaultdict(list)
        for h,i in enumerate(h2i):
            h2i[h].append(i)
        

        res = 0
        while l < r:

            area = min(heights[r], heights[l]) * (r - l)
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        