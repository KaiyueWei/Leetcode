class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        n = len(s)
        have = defaultdict(int)
        formed = 0
        shortest = math.inf
        pair = (-1, -1)

        l = 0

        for r in range(n):
            have[s[r]] += 1
            if s[r] in tCount and have[s[r]] == tCount[s[r]]:
                formed += 1
            while formed == len(tCount):
                w = r - l + 1
                if shortest > w:
                    shortest = w
                    pair = (l, r)
                have[s[l]] -= 1
                if s[l] in tCount and have[s[l]] < tCount[s[l]]:
                    formed -= 1
                l += 1
        if shortest == math.inf:
            return ""
        l, r = pair
        return s[l:r+1]

                
             