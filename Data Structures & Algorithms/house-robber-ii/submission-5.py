class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        def rob_line(arr):
            prev_2 = arr[0]
            prev_1 = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                cur = max(prev_2 + arr[i], prev_1)
                tmp = prev_1
                prev_1 = cur
                prev_2 = tmp
            return prev_1
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))

        