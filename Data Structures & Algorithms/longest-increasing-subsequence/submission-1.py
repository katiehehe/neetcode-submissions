class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_sub = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            next_max = 0
            for j in range(i + 1, len(nums)):
                next_max = max(next_max, longest_sub[j]) if nums[j] > nums[i] else next_max
            longest_sub[i] = 1 + next_max
        return max(longest_sub)
              