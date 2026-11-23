from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # value, count
        count = defaultdict(lambda: [0, 0])

        for n in nums:
            count[n][0] = n
            count[n][1] += 1 
        
        res = list(count.values())
        print(res)
        res = sorted(res, key=lambda x: x[1], reverse=True)
        print(res)
        return [x[0] for x in res[:k]]