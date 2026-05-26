class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n) * (n + 1) // 2
        pref_sum = 0
        for i in nums:
            pref_sum += i
        return total - pref_sum