class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = [0]

        def backtrack(curSum, index):
            if index == n:
                if curSum == target:
                    res[0] += 1
                return
            ways = [-1, 1]
            for w in ways:
                backtrack(curSum+w*nums[index], index+1)
        backtrack(0, 0)

        return res[0]

        