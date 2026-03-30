class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the mininum
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        min_index = l
        max_index = (l - 1) % n
        # two halves: 
        # 0 - max_index
        # min_index - n - 1
        if target > nums[max_index] or target < nums[min_index]:
            return -1
        elif target > nums[n-1]:
            i = 0
            j = max_index
        else:
            i = min_index
            j = n - 1     
        while i <= j:
            middle = (i+j) // 2
            if nums[middle] < target:
                i = middle + 1
            elif nums[middle] > target:
                j = middle - 1
            else:
                return middle
        return -1

        