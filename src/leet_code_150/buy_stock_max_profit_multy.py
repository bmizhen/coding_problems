from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        holding = -1

        for i in range(len(prices)):
            if holding != -1:
                if i == len(prices) - 1 or prices[i + 1] < prices[i]:
                    print('S', i, prices[i], holding)
                    profit += prices[i] - holding
                    holding = -1
            else:
                if i < len(prices) - 1 and prices[i + 1] > prices[i]:
                    print('B', i, prices[i], holding)
                    holding = prices[i]

        return profit
