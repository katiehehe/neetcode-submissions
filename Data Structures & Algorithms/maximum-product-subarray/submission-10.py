class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # check if no way to make positive, which happens iif no 2 consecutive pos / neg numbers
        pos = False
        for i in range(n - 1):
            if nums[i] > 0 or nums[i] * nums[i + 1] > 0:
                pos = True
        if nums[n - 1] > 0:
            pos = True
        if not pos:
            if n == 1:
                return nums[0]
            return 0
        globalMax = max(1, nums[n - 1])
        # base case
        maxSuf = max(1, nums[n - 1])
        minSuf = min(1, nums[n - 1])
        print(f"{maxSuf}, {minSuf}")
        # compute the max product starting from the end
        for i in range(n - 2, -1, -1):
            m = nums[i]
            if m >= 0:
                maxSuf = max(1, m * maxSuf)
                minSuf = min(1, m * minSuf)
            else:
                x = maxSuf
                maxSuf = max(1, m * minSuf)
                minSuf = min(1, m * x)
            print(f"{maxSuf}, {minSuf}")
            globalMax = max(globalMax, maxSuf)
        return globalMax
