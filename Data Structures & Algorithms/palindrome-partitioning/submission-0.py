class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        return False

    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def backtrack(currentPath, start):
            # base case: whole string consumed
            if start == n:
                res.append(currentPath)
                return

            # try all substrings starting at `start`
            for end in range(start + 1, n + 1):
                if self.isPalindrome(s[start:end]):
                    backtrack(currentPath + [s[start:end]], end)

        backtrack([], 0)
        return res

        