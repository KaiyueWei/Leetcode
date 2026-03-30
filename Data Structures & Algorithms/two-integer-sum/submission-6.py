class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = []
        for index, value in enumerate(nums):
            mapping.append([value, index])
        mapping.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            cur = mapping[l][0] + mapping[r][0]
            if cur == target:
                return [min(mapping[l][1], mapping[r][1]),
                        max(mapping[l][1], mapping[r][1])]
            elif cur < target:
                l += 1
            else:
                r -= 1
        return []

        
        