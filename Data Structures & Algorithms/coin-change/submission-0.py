class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minimum = [float('inf')] * (amount + 1)
        minimum[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    minimum[i] = min(minimum[i], minimum[i - c] + 1)
        return minimum[amount] if minimum[amount] < float('inf') else -1

        
        