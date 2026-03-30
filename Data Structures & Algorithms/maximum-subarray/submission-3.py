class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        prev = nums[0]
        for i in range(1, n):
            cur = max(prev + nums[i], nums[i])
            prev = cur
            res = max(cur, res)
        return res
            
        