class Solution:
    def isPalindrome(self, s:str, start: int, end: int) -> bool:
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return self.isPalindrome(s, start+1, end -1)
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def backtrack(currentPath, start):
            if start == n:
                res.append(currentPath)
                return 
            for end in range(start, n):
                if self.isPalindrome(s, start, end):
                    backtrack(currentPath + [s[start: end+1]], end+1)
        backtrack([], 0)
        return res
        