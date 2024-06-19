from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = 0
        for p in prices:
            current_min = min(current_min, p)
            max_profit = max(p - current_min, max_profit)
        return max_profit
