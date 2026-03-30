class Solution:
    def isPalindrome(self, s: str) -> bool:
        #get the alphanumeric of the string
        alpha_num = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                alpha_num += c
        alpha_num = alpha_num.lower()
        #check if it's a palindrome
        length = len(alpha_num)
        if length == 0 or length == 1:
            return True
        l, r = 0, length - 1
        while l < r:
            if alpha_num[l] != alpha_num[r]:
                return False
            l, r = l + 1, r - 1
        return True

        