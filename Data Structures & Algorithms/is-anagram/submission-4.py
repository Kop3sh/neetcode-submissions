from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
        for c in t:
            chars[c] -= 1
        
        for _, v in chars.items():
            if v != 0:
                return False
        return True


        