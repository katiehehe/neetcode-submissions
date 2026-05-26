class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            prof = max(prof, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
        return prof