class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        new_string = ""
        for c in s:
            if c.isalpha():
                new_string += c.lower()
            elif c.isdigit():
                new_string += c
        n = len(new_string)
        for i in range(n // 2):
            if new_string[i] != new_string[n - 1 - i]:
                return False
        return True
        