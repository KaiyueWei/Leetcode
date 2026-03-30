class Solution:
    def countBits(self, n: int) -> List[int]:
        # n & n - 1 removes the last 1 bit
        # dp[n] = dp[n & n - 1] + 1
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i & (i-1)] + 1
        return dp
        