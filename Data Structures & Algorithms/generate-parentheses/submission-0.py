class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openP, closeP, current):
            if len(current) == 2 * n:
                res.append(current)
            
            # choice 1: add "("
            if openP < n:
                backtrack(openP + 1, closeP, current + "(")

            # choice 2: add ")"
            if closeP < openP:
                backtrack(openP, closeP + 1, current + ")")

        backtrack(0, 0, "")
        return res
            

                
