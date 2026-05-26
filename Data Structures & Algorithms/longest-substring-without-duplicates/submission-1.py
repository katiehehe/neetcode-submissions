class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ptr1 = 0
        ptr2 = 1
        chars = {s[0]}
        max_len = 1
        while ptr1 < len(s):
            while ptr2 < len(s) and s[ptr2] not in chars:
                chars.add(s[ptr2])
                ptr2 += 1
            max_len = max(max_len, ptr2 - ptr1)
            chars.remove(s[ptr1])
            ptr1 += 1
        return max_len