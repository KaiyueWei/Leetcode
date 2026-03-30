class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum // 2
        def backtrack(start, curSum):
            if curSum == target:
                return True
            if curSum > target:
                return False

            for i in range(start, n):
                if backtrack(i+1, curSum + nums[i]):
                    return True

            return False

        return backtrack(0, 0)


        