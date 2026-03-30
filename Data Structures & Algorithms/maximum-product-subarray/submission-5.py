class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        maxCur = nums[0]
        minCur = nums[0]
        res = float('-inf')

        for i in range(1, n):
            extendMin = minCur * nums[i]
            extendMax = maxCur * nums[i]
            cur = nums[i]
            maxCur = max(extendMax, extendMin, cur)
            minCur = min(extendMax, extendMin, cur)
            res = max(maxCur, res)
        return res
            
        