class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        second = 1
        first = 1 if 1 <= int(s[n - 1]) <= 9 else 0
        for i in range(n - 2, -1, -1):
            cur = 0
            if 1 <= int(s[i]) <= 9:
                cur = first
            if 10 <= int(s[i] + s[i + 1]) <= 26:
                cur += second
            second = first
            first = cur
        return first

