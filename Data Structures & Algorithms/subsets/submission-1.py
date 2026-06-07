class Solution:

    def backtrack(self, index, candidates, path, result):
        # base case
        if index >= len(candidates):
            result.append([element for element in path])
            return 
        # option1: include the current candidate
        path.append(candidates[index])
        self.backtrack(index+1, candidates, path, result)
        path.pop()
        # option2: do not include the current candidate
        self.backtrack(index+1, candidates, path, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(0, nums, [], result)
        return result
        