class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        local_max = nums[0]
        local_min = nums[0]
        global_max = max(nums[0], float('-inf'))
        for i in range(1, n):
            cur = nums[i]
            extend_max = local_max * cur
            extend_min = local_min * cur
            not_extend = cur
            local_max = max(extend_max, extend_min, not_extend)
            local_min = min(extend_max, extend_min, not_extend)
            global_max = max(local_max, global_max, local_min)
        return global_max

        