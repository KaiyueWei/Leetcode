class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        while(len(res) <= n):
            res.extend( [i + 1 for i in res])
        return res[:n+1]