class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        prod1 = 1
        prod2 = 1
        for i in range(len(nums)):
            prod1 *= nums[i]
            pref.append(prod1)
            prod2 *= nums[len(nums) - 1 - i]
            suff.append(prod2)
        final_lst = []
        for i in range(len(nums)):
            final_lst.append(pref[i] * suff[len(nums) - i - 1])
        return final_lst

        