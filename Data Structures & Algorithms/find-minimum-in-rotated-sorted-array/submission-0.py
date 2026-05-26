class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = nums[len(nums) - 1]
        lo = -1
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if nums[mid] > end:
                lo = mid
            else:
                hi = mid - 1
        return nums[lo + 1]