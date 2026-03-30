class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize index_i and index_j
        index_i = None
        index_j = None
        #iterate from i and 
        #check if the next number adds number i equals target
        for i in range(len(nums)):
            index_i = i
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_j = j
                    return [i, j]
                else:
                    continue
        
        