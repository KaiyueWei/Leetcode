class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize a dict to store the value visited
        #key is the value and value is the index
        mapping = dict()
        for i in range(len(nums)):
            other = target - nums[i]
            other_index = mapping.get(other, None)
            if other_index != None:
                return [other_index, i]
            else:
                mapping[nums[i]] = i
                continue
                
        