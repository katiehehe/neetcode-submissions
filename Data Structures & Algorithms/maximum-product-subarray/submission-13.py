class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        globalMax = nums[n - 1]
        # base case
        maxSuf = 1
        minSuf = 1
        # compute the max product starting from the end
        for i in range(n - 1, -1, -1):
            m = nums[i]
            x = maxSuf
            maxSuf = max(m, m * minSuf, m * maxSuf)
            minSuf = min(m, m * minSuf, m * x)
            globalMax = max(globalMax, maxSuf)
        return globalMax
