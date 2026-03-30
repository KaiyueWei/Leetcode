class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(path, used):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used.remove(i)

        backtrack([], set())
        return res
        