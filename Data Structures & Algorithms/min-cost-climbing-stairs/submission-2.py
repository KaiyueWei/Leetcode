class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 0

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            dp[i] = min(cost[i-1] + dfs(i-1), cost[i-2] + dfs(i-2))
            return dp[i]

        return dfs(n)
        