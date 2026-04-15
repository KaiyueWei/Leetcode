class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        longest = 0
        res = ""
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j -i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    w = j - i + 1
                    if w > longest:
                        longest = w
                        res = s[i:j+1]
        return res

        