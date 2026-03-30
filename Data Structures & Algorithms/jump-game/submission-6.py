class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {n-1:True}
        def can_reach(i):
            if i in dp:
                return dp[i]
            for jump in range(1, nums[i]+1):
                if can_reach(i+jump):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return can_reach(0)    