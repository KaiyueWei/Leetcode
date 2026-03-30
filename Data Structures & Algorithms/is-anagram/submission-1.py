class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_s = dict()
        mapping_t = dict()
        for c in s:
            if mapping_s.get(c, None) != None:
                mapping_s[c] += 1
            else:
                mapping_s[c] = 1     
        for c in t:
            if mapping_t.get(c, None) != None:
                mapping_t[c] += 1
            else:
                mapping_t[c] = 1               
        if mapping_s == mapping_t:
            return True
        else:
            return False
