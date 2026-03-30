class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        res = 0
        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        for j in range(n-2,-1,-1):
            rightMax[j] = max(rightMax[j+1],height[j+1])
        
        for i in range(n):
            s = min(leftMax[i], rightMax[i]) - height[i]
            if s > 0:
                res += s
        return res





            
            


    



        