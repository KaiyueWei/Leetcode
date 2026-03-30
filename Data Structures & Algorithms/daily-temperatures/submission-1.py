class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] 

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stack_i, stack_t = stack.pop()
                result[stack_i] = i - stack_i
            stack.append((i, t))
        return result
        