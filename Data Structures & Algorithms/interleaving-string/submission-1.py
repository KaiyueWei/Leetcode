class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        t = len(s3)

        if t != n + m:
            return False
        
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True

        for i in range(1, n+1):
            if s1[i-1] == s3[i-1]:
                dp[0][i] = True
        
        for j in range(1, m+1):
            if s2[j-1] == s3[j-1]:
                dp[j][0] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s3[i+j-1] == s1[j-1]:
                    dp[i][j] = dp[i][j-1]
                elif s3[i+j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n]


        