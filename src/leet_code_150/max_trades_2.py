from itertools import accumulate


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price_before = accumulate(prices, min)
        max_price_after = reversed(list(accumulate(
            reversed(prices), max)))

        max_before = 0
        max_trade_before = [
            max_before := max(max_before, p - min_price)
            for p, min_price in zip(prices, min_price_before)
        ]

        max_after = 0
        max_trade_after = reversed([
            max_after := max(max_after, max_price - p)
            for p, max_price in reversed(list(zip(prices, max_price_after)))
        ])

        return max(before + after
                   for before, after
                   in zip(max_trade_before, max_trade_after))
