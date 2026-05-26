class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums)
        start = nums[0]
        while f < l:
            m = (f + l) // 2
            if nums[m] >= start:
                f = m + 1
            else:
                l = m
        if l == len(nums):
            f = 0
        else: 
            f = l
        l = f + len(nums) - 1
        while f <= l:
            m = (f + l) // 2
            if nums[m % len(nums)] == target:
                return m % len(nums)
            if nums[m % len(nums)] > target:
                l = m - 1
            else:
                f = m + 1
        return -1

