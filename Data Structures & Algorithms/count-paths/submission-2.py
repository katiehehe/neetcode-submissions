class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        bot = min(m - 1, n - 1)
        res = 1
        for i in range(1, bot + 1):
            res *= ((i + total - bot) / i)
        return round(res)