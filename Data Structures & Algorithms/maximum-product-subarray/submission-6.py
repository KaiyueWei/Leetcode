class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max = nums[0]
        local_min = nums[0]
        global_max = max(local_max, local_min)

        for i in range(1, len(nums)):
            extMax = local_max * nums[i]
            extMin = local_min * nums[i]
            cur = nums[i]
            local_max = max(extMax, extMin, cur)
            local_min = min(extMax, extMin, cur)
            global_max = max(global_max, local_max)
        return global_max

        