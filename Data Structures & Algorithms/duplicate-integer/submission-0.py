class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for n in nums:
            if n in elements:
                return True
            elements.add(n)
        return False