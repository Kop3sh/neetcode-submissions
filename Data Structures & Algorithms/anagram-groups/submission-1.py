from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            k = str(sorted(s))
            res[k].append(s)


        return [v for k, v in res.items()]
        