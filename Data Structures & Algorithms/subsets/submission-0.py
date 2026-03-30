class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(currentPath, start):
            res.append(currentPath)
            for i in range(start, n):
                backtrack(currentPath + [nums[i]], i + 1)

        
        backtrack([], 0)
        return res