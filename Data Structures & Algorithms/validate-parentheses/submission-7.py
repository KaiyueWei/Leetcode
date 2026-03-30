class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for c in s:
            if c in mapping.keys():
                stack.append(c)
            else:
                if stack and mapping[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        