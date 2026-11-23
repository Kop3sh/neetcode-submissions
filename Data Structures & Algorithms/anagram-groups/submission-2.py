from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # # o(n)
        # for s in strs:
        #     # O(nlogn)
        #     k = str(sorted(s))
        #     res[k].append(s)
        # return [v for k, v in res.items()]
        def counter(w):
            reps = [0] * 26
            for _, c in enumerate(w):
                i = ord(c) - ord('a')
                reps[i] += 1
            return str(reps)


        res = defaultdict(list)
        for s in strs:
            k = counter(s)
            res[k].append(s)

        return [v for k, v in res.items()]
        