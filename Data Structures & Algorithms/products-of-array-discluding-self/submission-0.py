class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the product of all the elements
        # edge case: 0
        zeros_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_index.append(i)
        all_product = 1
        res = [ 0 ] * len(nums)
        if len(zeros_index) == 0:
            for i in range(len(nums)):
                all_product = all_product * nums[i]
            for i in range(len(nums)):
                res[i] = (all_product // nums[i])
        elif len(zeros_index) == 1:
            for i in range(len(nums)):
                if i == zeros_index[0]:
                    continue
                all_product = all_product * nums[i]
            res[zeros_index[0]] = all_product
        return res



        