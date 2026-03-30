class Solution:
    def isValid(self, s: str) -> bool:
        # a stack of opening brackets
        # the last in opening bracket should be closed first
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            # if c is closing bracket
            if c in pairs.keys():
                # if there is no opening bracke
                # or the last in bracket is not the corresponding bracket
                if not stack or pairs[c] != stack[-1]:
                    return False
                # close the most recently bracket
                else:
                    stack.pop()
            # if c is opening bracket, add to the stack
            else:
                stack.append(c)
        # every opening bracket should be closed properly
        # if the stack is empty, there are brackets left
        if not stack:
            return True
        return False
