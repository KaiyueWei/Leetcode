class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # only start if it's the beginning of a sequence
            if num - 1 not in numSet:
                length = 1
                cur = num

                while cur + 1 in numSet:
                    cur += 1
                    length += 1

                longest = max(longest, length)

        return longest