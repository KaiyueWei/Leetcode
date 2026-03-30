class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        l, r = 0, 0
        window = set()
        for r in range(n):
            if s[r] in window:
                while l < r and s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
            w = r - l + 1
            longest = max(longest, w)
        return longest

        