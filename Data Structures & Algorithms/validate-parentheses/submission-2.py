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
            if c in pairs.keys():
                if not stack or pairs[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if not stack:
            return True
        return False
