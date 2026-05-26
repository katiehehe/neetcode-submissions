class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_set = set()
        index = 0
        while index < len(nums) and nums[index] <= 0:
            goal_sum = -nums[index]
            ptr1 = index + 1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                if nums[ptr1] + nums[ptr2] == goal_sum:
                    final_set.add((nums[index], nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
                elif nums[ptr1] + nums[ptr2] > goal_sum:
                    ptr2 -= 1
                else:
                    ptr1 += 1
            index += 1
        return [list(ls) for ls in final_set]