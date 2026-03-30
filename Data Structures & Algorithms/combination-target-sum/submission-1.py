class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(currentPath, currentList, sum1):
            if sum1 == target:
                res.append(currentPath)
                return
            elif sum1 > target:
                return
            else:
                for i in range(len(currentList)):
                    sum1 += currentList[i]
                    backtrack(currentPath + [currentList[i]], currentList[i:], sum1)
                    sum1 -= currentList[i]
        backtrack([], nums, 0)
        return res

        