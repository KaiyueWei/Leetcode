class Solution:
    def climbStairs(self, n: int) -> int:
        prev_1 = 1
        prev_2 = 1

        for i in range(2, n+1):
            cur = prev_1 + prev_2
            tmp = prev_1
            prev_1 = cur
            prev_2 = tmp
        return prev_1

        