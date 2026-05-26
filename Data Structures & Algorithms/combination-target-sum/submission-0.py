class Solution:
    def combo_sum_helper(self, nums, target, end):
        end_num = nums[end]
        final_list = []
        if end == 0:
            if target % end_num == 0:
                final_list.append([end_num] * (target // end_num))
            return final_list
        for i in range(target // end_num + 1):
            small = self.combo_sum_helper(nums, target - i * end_num, end - 1)
            if len(small) != 0:
                for pos in small:
                    pos.extend([end_num] * i)
                    final_list.append(pos)
        return final_list
        


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.combo_sum_helper(nums, target, len(nums) - 1)