class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # XOR = sum of bits, AND<<1 = carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # if a is negative in 32-bit signed form
        return a if a <= MAX_INT else ~(a ^ MASK)
