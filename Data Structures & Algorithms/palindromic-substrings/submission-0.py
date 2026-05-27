class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # 1st count odd-length palindromes from a center
        for i in range(len(s)):
            j = 0
            while j < min(i + 1, len(s) - i):
                if s[i - j] == s[i + j]:
                    count += 1
                    j += 1
                else:
                    break
        # count even-length palindromes
        for i in range(len(s) - 1):
            j = 0
            while j < min(i + 1, len(s) - i - 1):
                if s[i - j] == s[i + 1 + j]:
                    count += 1
                    j += 1
                else:
                    break
        return count
