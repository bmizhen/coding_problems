# https://leetcode.com/problems/ipo/

from heapq import *


class Solution:
    def findMaximizedCapital(
            self, k: int, w: int,
            profits: list[int], capital: list[int]) -> int:

        max_profit_up_to_given_start_capital = []

        projects = list(sorted([
            (cap, prof) for cap, prof in zip(capital, profits)]))
        projects_index = 0
        capital = w

        for _ in range(k):
            while projects_index < len(projects):
                cap, prof = projects[projects_index]
                if cap <= capital:
                    heappush(max_profit_up_to_given_start_capital,
                             -prof)
                    projects_index += 1
                else:
                    break
            if not max_profit_up_to_given_start_capital:
                break

            capital += - heappop(max_profit_up_to_given_start_capital)

        return capital
