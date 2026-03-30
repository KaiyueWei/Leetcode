class Solution:     
    def isPalindrome(self, s: str) -> bool:
        ## process the string
        ## only keep alphabetics
        lower_s = s.lower()
        print(lower_s)
        new_s = ""
        for c in lower_s:
            if (ord('a') <= ord(c) and \
                ord(c) <= ord('z')):
                new_s += c
            if (ord('0') <= ord(c) and \
                ord(c) <= ord('9')):
                new_s += c
        print(new_s)
        n = len(new_s)
        def helper(l:int, r:int) -> bool:
            if l >= r:
                return True
            if new_s[l] != new_s[r]:
                return False
            return helper(l+1, r-1)
        l, r = 0, n - 1
        return helper(0, n-1)



        