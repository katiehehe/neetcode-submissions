class Solution:
    def rob(self, nums: List[int]) -> int:
        best_arr = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            best_arr[i + 2] = max(best_arr[i + 1], best_arr[i] + nums[i])
        return max(best_arr)
