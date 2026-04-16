class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                start = num
                length = 0
                while start + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        