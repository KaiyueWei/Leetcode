class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        ## starting point pointing to the first letter
        ## if the next letter is consecutive, go on until there is a repeat
        ## or it's not consecutive anymore
        i = 0
        while i < len(s):
            cur = 1
            start = i
            end = i
            j = start + 1
            if j < len(s) and (s[j] not in s[start:end+1]):
                while j < len(s) and (s[j] not in s[start:end+1]):
                    j += 1
                    end += 1
                cur = end + 1 - start 
            res = max(cur, res)
            i += 1 
        return res
    



        