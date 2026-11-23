class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            tmp = 0
            while i != 0:
                i = i & (i - 1)
                tmp += 1
            res.append(tmp)
        return res
        