class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ## keep track of the global maximum
        res = nums[0]
        ## keep track of the maxium ending at index i - 1
        prev = nums[0]
        ## iterate through from 1 to n - 1
        for i in range(1, n):
            ## at each index i
            ## option1: starting a new subarray at index i
            ## option2: extend the previous subrray ending at index i - 1
            ## to index i
            cur = max(prev + nums[i], nums[i])
            ## update the prev
            prev = cur
            ## check the global maximum
            res = max(cur, res)
        return res
            
        