class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize a dict to store the value visited
        #key is the value and value is the index
        prevMapping = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMapping:
                return [prevMapping[diff], i]
            prevMapping[num] = i
        return
                
        