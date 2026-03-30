class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(currentPath, start, sum1):
            if sum1 == target:
                res.append(currentPath)
                return 
            elif sum1 > target:
                return
            else:
                for i in range(start, n):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    sum1 += candidates[i]
                    backtrack(currentPath + [candidates[i]], i + 1, sum1)
                    sum1 -= candidates[i]
        
        backtrack([], 0, 0)
        return res
        