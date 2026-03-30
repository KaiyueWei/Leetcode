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
        for i in range(length // 2):
            j = length - 1 - i
            if alpha_num[i] == alpha_num[j]:
                continue
            return False
        return True

        