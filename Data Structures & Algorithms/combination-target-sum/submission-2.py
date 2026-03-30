class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(curPath, start, curSum):
            if curSum == target:
                res.append(curPath)
            elif curSum > target:
                return
            else:
                for i in range(start, n):
                    curSum += nums[i]
                    backtrack(curPath +[nums[i]], i, curSum)
                    curSum -= nums[i]
        backtrack([], 0, 0)
        return res 

        