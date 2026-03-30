class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean the string
        new_s = ""
        for i in range(len(s)):
            c = s[i]
            if ord('A') <= ord(c) <= ord('Z') or \
                ord('a') <= ord(c) <= ord('z') or \
                ord('0') <= ord(c) <= ord('9'):
                new_s += c
        new_s = new_s.lower()
        n = len(new_s)
        l = 0
        r = n - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True