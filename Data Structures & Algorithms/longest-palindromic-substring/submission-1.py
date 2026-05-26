class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        cent = 0
        # check odd-length permutations
        for center in range(len(s)):
            extend = 1 # exclusive
            while extend <= center < len(s) - extend:
                if s[center - extend] == s[center + extend]:
                    extend += 1
                else:
                    break
            if extend > longest:
                cent = center
            longest = max(longest, extend)
        # check even-length permutations
        max_even = 0
        ecenter = 0
        for lcenter in range(len(s) - 1):
            if s[lcenter + 1] != s[lcenter]:
                continue
            curr = 1
            while curr <= lcenter < len(s) - curr - 1:
                if s[lcenter - curr] == s[lcenter + curr + 1]:
                    curr += 1
                else:
                    break
            if curr > max_even:
                max_even = curr
                ecenter = lcenter
        if 2 * max_even > 2 * longest - 1:
            return s[ecenter - max_even + 1: ecenter + max_even + 1]
        return s[cent - longest + 1: cent + longest]