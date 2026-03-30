class Solution:
    def helper(self, s: str) -> bool:
        length = len(s)
        if length == 0 or length == 1:
            return True
        if s[0] == s[length-1]:
            return self.helper(s[1:length-1])
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        #get the alphanumeric of the string
        alpha_num = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                alpha_num += c
        alpha_num = alpha_num.lower()
        #check if it's a palindrome
        return self.helper(alpha_num)


        