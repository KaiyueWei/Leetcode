class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## an array of buckets, index : frequency
        ## each bucket is an array of numbers that have the same frequency
        buckets = [[] for _ in range(len(nums)+1)]
        ## get the frequency of each number
        freqs = {}
        for i in range(len(nums)):
            freqs[nums[i]] = 1 + freqs.get(nums[i], 0)
        for num, freq in freqs.items():
            buckets[freq].append(num)
        ## extract top k
        i = 1 # number of distinct values
        j = 0
        res = []
        while i <= k:
            index = len(nums) - j
            if len(buckets[index]) == 0:
                j += 1
                continue
            else:
                res += buckets[index]
                i += len(buckets[index])
                j += 1
        return res



        