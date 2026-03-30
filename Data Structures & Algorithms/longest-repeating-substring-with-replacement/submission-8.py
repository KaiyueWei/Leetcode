class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        res = 0
        n = len(s)
        l = 0
        for r in range(n):
            # add the cur charater to the freq
            freq[ord(s[r])-ord('A')] += 1
            # check if it satisfies the constraint 
            w = r - l + 1
            while l < n - 2 and w - max(freq) > k:
                freq[ord(s[l])-ord('A')] -= 1
                l += 1
                w = r - l + 1
            res = max(res, w)
        return res



