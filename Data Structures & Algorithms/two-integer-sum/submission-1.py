class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate from i and 
        #check if the next number adds number i equals target
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    continue
        
        