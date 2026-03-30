class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        min_index = l
        max_index = (min_index - 1) % n

        if target < nums[min_index] or target > nums[max_index]:
            return -1
        else:
            if target <= nums[n-1]:
                l = min_index
                r = n - 1
            else:
                l = 0
                r = max_index
        
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1 
            
    