class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {} #number: occurence
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        res = [0] * len(nums)
        global_max = 0
        for i in range(len(nums)):
            cur_max = 1
            j = nums[i] + 1
            # find the numbers are greater than nums[i]
            while freq.get(j, 0) != 0:
                cur_max += 1
                j += 1
            z = nums[i] - 1
            # find the numbers are less than nums[i]
            while freq.get(z, 0) != 0:
                cur_max += 1
                z -= 1
            res[i] = cur_max
            if global_max < cur_max:
                global_max = cur_max
        return global_max
            