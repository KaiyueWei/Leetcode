class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            n = len(arr)
            if n <= 1:
                return arr[0]
            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])
            for i in range(2, n):
                cur = max(prev1, prev2+arr[i])
                prev2 = prev1
                prev1 = cur
            return prev1
        
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
        