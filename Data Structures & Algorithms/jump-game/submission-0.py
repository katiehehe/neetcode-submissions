class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lowest_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lowest_index:
                lowest_index = i
        return lowest_index == 0
