class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            print(i)
            cur = 1
            start = i
            end = i
            j = start + 1
            if j < len(s) and (s[j] not in s[start:end+1]):
                while j < len(s) and (s[j] not in s[start:end+1]):
                    j += 1
                    end += 1
                cur = end + 1 - start
            if j < len(s):
                i = 1 + start + s[start:end+1].index(s[j])
            else:
                i += 1
            res = max(cur, res)
        return res
    



        