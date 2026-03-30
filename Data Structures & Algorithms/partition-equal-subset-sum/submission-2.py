class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        p = total // 2

        dp = [False] * (p+1)
        dp[0] = True

        for num in nums:
            for i in range(p, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[p]
                