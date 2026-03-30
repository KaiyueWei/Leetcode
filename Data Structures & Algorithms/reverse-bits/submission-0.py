class Solution:
    def reverseBits(self, n: int) -> int:
        output, power = 0, 31

        while n:
            output += (n&1) << power
            n = n >> 1
            power -= 1
        return output