class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVisited = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevVisited.keys():
                return [prevVisited[diff], index]
            prevVisited[value] = index
        return 
        
        