class Solution:     
    def isPalindrome(self, s: str) -> bool:
        ## process the string
        ## only keep alphabetics
        lower_s = s.lower()
        new_s = ""
        new_s = ''.join(c for c in lower_s if c.isalnum())
        n = len(new_s)
        def helper(l:int, r:int) -> bool:
            if l >= r:
                return True
            if new_s[l] != new_s[r]:
                return False
            return helper(l+1, r-1)
        l, r = 0, n - 1
        return helper(0, n-1)



        