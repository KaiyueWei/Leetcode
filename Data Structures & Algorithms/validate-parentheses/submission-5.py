class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n == 0:
            return True
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack:
                    last = stack[-1]
                    if c == ')' and last == '(':
                        stack.pop()
                    elif c == ']' and last == '[':
                        stack.pop()
                    elif c == '}' and last == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
        