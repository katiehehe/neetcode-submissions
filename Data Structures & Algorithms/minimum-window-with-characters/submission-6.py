class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        minLength = len(s) + 1
        freq = {}
        left, right = 0, 0

        # setup the dictionary for t
        charCount = {}
        for c in t:
            charCount[c] = charCount.get(c, 0) + 1
        def validStr(frequency):
            for c in charCount:
                if frequency.get(c, 0) < charCount[c]:
                    return False
            return True

        while r < len(s):
            # evaluate the current string
            print(f"{l} and {r}")
            
            if not validStr(freq):
                freq[s[r]] = freq.get(s[r], 0) + 1
                r += 1
            else:
                if r - l < minLength:
                    minLength = r - l
                    left = l
                    right = r
                freq[s[l]] -= 1
                l += 1

        if validStr(freq):
            print("true")
            # keep moving the left pointer
            while l < len(s):
                if s[l] not in t or freq[s[l]] > charCount[s[l]]:
                    freq[s[l]] -= 1
                    l += 1
                else:
                    break
            if r - l < minLength:
                minLength = r - l
                left = l
                right = r
        if minLength == len(s) + 1:
            return ""
        return s[left: right]
 
