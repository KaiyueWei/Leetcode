class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum // 2

        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for s in range(target, num-1, -1):
                dp[s] = dp[s] or dp[s-num]
        return dp[target]
        