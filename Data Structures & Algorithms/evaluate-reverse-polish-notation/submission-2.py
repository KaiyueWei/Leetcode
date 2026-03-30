class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for i in range(len(tokens)):
            t = tokens[i]
            print(f'{t}')
            print(f'{stack}')
            if not stack:
                stack.append(int(t))
                continue
            
            if t in ops:
                last = stack.pop()
                prev = stack.pop()
                if t == '+':
                    stack.append(last+prev)
                elif t == '-':
                    stack.append(prev-last)
                elif t == '*':
                    stack.append(prev*last)
                else:
                    stack.append(int(prev/last))
            else:
                stack.append(int(t))
        return stack[0]