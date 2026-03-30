class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        prev1 = max(nums[1], nums[0])
        prev2 = nums[0]

        for i in range(2, n):
            cur = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = cur

        return prev1
            
        