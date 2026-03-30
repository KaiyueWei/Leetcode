class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        for i in range(n-1):
            cur = temperatures[i]
            j = i + 1
            while j < n and temperatures[j] <= cur:
                j += 1
            if j < n and temperatures[j] > cur:
                result[i] = j - i
            else:
                result[i] = 0
        
        return result
            
        