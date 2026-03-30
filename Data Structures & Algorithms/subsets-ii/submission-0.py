class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(currentPath, start):
            res.append(currentPath)
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(currentPath + [nums[i]], i + 1)
        backtrack([], 0)
        return res
        