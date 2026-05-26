class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0, 0
        max_rob = 0
        for i in range(len(nums) - 1):
            temp_max = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp_max
            max_rob = max(max_rob, rob2)
        rob1, rob2 = 0, 0
        max_rob2 = 0
        for i in range(1, len(nums) - 2):
            temp_max = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp_max
            max_rob2 = max(max_rob2, rob2)
        return max(max_rob, max_rob2 + nums[-1])