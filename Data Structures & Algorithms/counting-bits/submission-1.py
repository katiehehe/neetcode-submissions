class Solution:
    def countBits(self, n: int) -> List[int]:
        final = [0] * (n + 1)
        for i in range(1, n + 1):
            if final[i] == 0:
                final[i] = final[i - 1] + 1
                ptr = 2 * i
                while ptr <= n:
                    final[ptr] = final[i]
                    ptr *= 2
        return final