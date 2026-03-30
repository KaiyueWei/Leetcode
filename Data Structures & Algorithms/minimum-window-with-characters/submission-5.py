class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)
        if len_s < len_t:
            return ""
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        have = defaultdict(int)
        matched = 0
        shortest = math.inf
        res = ""
        l = 0
        for r in range(len_s):
            print(f'r{r}')
            cur = s[r]
            have[cur] += 1
            if cur in target and have[cur] == target[cur]:
                matched += 1
            while matched == len(target):
                w = r - l + 1
                if w < shortest:
                    shortest = w
                    res = s[l:r+1]
                have[s[l]] -= 1
                if s[l] in target and have[s[l]] < target[s[l]]:
                    matched -= 1
                l += 1
        return res
        




                
             