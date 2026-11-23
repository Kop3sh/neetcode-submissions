class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        target = float('inf') 
        while l <= r:
            m = ( l + r ) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                if nums[m] < target:
                    target = nums[m]
                    r = m - 1
                else:
                    l = m + 1

        return target
                
                

        