class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        counts = {}
        counts[s[right]] = counts.get(s[right], 0) + 1
        right += 1
        maxLen = 1
        while right < len(s):
            # if the current count is <=k, we keep adding
            print(right - left - max(counts.values()))
            if right - left - max(counts.values()) <= k:
                maxLen = max(maxLen, right - left)
                counts[s[right]] = counts.get(s[right], 0) + 1
                right += 1
            else:
                counts[s[left]] -= 1
                left += 1
            print(f"{left} and {right}")
        if right - left - max(counts.values()) <= k:
                maxLen = max(maxLen, right - left)
        return maxLen


            