class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []
        # for i in range(n+1):
        #     tmp = 0
        #     while i != 0:
        #         i = i & (i - 1)
        #         tmp += 1
        #     res.append(tmp)
        # return res

        dp = [0] * (n+1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

        for i in range(1, n+1):
            dp[i] = dp[i>>1] + (i & 1)
        return dp
        