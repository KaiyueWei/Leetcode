class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        have = defaultdict(int)
        need = len(tCount)
        formed = 0

        shortest = math.inf
        pair = (-1, -1)

        l = 0
        n = len(s)

        for r in range(n):
            c = s[r]
            have[c] += 1
            if c in tCount and have[c] == tCount[c]:
                formed += 1
            
            while formed == need:
                w = r - l + 1
                if w < shortest:
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

                
             