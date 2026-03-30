class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def backtrack(curPath, start, curSum):
            if curSum == target:
                res.append(curPath)
            elif curSum > target:
                return 
            else:
                for i in range(start, n):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    curSum += candidates[i]
                    backtrack(curPath+[candidates[i]], i+1, curSum)
                    curSum -= candidates[i]
        backtrack([], 0, 0)
        return res
        
        