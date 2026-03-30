class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        res = 0
        l = 0
        for r in range(n):
            c = s[r]
            while c in seen and l < n - 1:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            res = max(res, r - l + 1)
        return res
        



        