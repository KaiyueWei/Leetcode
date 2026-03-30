class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+',
            '-',
            '/',
            '*',
        }

        for t in tokens:
            if stack and t in operators:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(a-b)
                    case '*':
                        stack.append(a*b)
                    case _:
                        stack.append(int(a/b))
            else:
                stack.append(int(t))
        return stack[0]



        