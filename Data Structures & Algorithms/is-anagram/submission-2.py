from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = dict()
        t_map = dict()

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        for k, v in s_map.items():
            if k not in t_map:
                return False
            if s_map[k] != t_map[k]:
                return False
        
        return True
