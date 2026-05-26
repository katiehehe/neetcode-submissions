class Solution:
    def reverseBits(self, n: int) -> int:
        final_num = 0
        for i in range(32):
            final_num *= 2
            final_num += (n >> i) & 1
        return final_num