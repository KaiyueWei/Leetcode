class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## count the frequency of value
        ## key: number, value: the frequency of the number
        freq_pairs = dict()
        ## get the length of the list
        length = len(nums)
        ## iterate the list to get the frequency of each value
        for i in range(length):
            key = nums[i]
            ## if key exists, return True
            if freq_pairs.get(key, None) != None:
                return True
            else:
                freq_pairs[key] = 1
        ## return False if we exit out of the loop
        return False
        
        