class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        i_2 = 1
        i_1 = 1 if s[0] != '0' else 0

        for i in range(2, n+1):
            cur = 0
            if s[i-1] != '0':
                cur += i_1
            if (s[i-2] == '1' or
                (s[i-2] == '2' and s[i-1] < '7')):
                cur += i_2
            i_2 = i_1
            i_1 = cur
        return i_1
        