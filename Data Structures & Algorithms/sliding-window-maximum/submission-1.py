class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        window = []
        l = 0
        for r in range(n):
            window.append(nums[r])

            while r - l + 1 > k:
                window.remove(nums[l])
                l += 1
            
            if r - l + 1 == k:
                res.append(max(window))
        
        return res


        