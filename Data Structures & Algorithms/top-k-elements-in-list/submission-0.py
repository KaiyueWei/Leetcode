class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##get the frequency of num
        freq = {} #value:frequency
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        ##sort the dict in descending order with comparison key frequency
        sorted_freq = sorted(freq.items(), key=lambda item : item[1], reverse=True)
        ##take the top k frequent values
        res = []
        for i in range(k):
            res.append(sorted_freq[i][0])
        return res



        