class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                return [l+1, r+1]



        