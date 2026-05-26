class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_pref = 0
        curr = 0
        max_sub = nums[0]
        for num in nums:
            curr += num
            max_sub = max(max_sub, curr - min_pref)
            min_pref = min(min_pref, curr)
        return max_sub