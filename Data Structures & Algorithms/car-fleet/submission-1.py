class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speeds = list(zip(position, speed))
        position_speeds.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for p, s in position_speeds:
            t = (target - p) / s
            if stack and stack[-1] >= t:
                continue
            else:
                stack.append(t)

        return len(stack)


        