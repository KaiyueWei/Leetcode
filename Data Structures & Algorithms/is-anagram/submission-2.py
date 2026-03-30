class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_s, mapping_t = {}, {}
        for i in range(len(s)):
            mapping_s[s[i]] = mapping_s.get(s[i], 0) + 1
            mapping_t[t[i]] = mapping_t.get(t[i], 0) + 1            
        return mapping_s == mapping_t