class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        window = defaultdict(int)
        formed = 0
        l = 0
        n = len(s)
        shortest = math.inf
        pair = (-1, -1)

        for r in range(n):
            c = s[r]
            print(f'c:{c}')
            window[c] += 1
            if c in tCount and window[c] == tCount[c]:
                formed += 1
            print(f'formed:{formed}')
            while formed == len(tCount):
                w = r - l + 1
                print(f'w:{w}')
                if w < shortest:
                    shortest = w
                    pair = (l, r)
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    formed -= 1
                l += 1
        if shortest == math.inf:
            return ""
        l, r = pair
        return s[l:r+1]

                
             