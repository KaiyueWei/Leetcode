class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] + a < 0:
                    l += 1
                elif nums[l] + nums[r] + a > 0:
                    r -= 1
                else:
                    res.add(tuple(sorted([a, nums[l], nums[r]])))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return [list(i) for i in res]
                

            
                



        
        