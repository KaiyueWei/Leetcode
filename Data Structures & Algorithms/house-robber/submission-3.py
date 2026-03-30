class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        prev_2 = nums[0]
        prev_1 = max(nums[0], nums[1])

        if n == 2:
            return max(prev_1, prev_2)

        for i in range(2, n):
            cur = max(prev_2 + nums[i], prev_1)
            tmp = prev_1 
            prev_1 = cur
            prev_2 = tmp
        return prev_1
        