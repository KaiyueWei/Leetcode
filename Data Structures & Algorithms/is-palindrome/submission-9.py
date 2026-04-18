class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        if newStr == "":
            return True
        if len(newStr) == 1:
            return True
        
        l = 0
        r = len(newStr) - 1
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True