import itertools


class Solution:
    def trap(self, height: list[int]) -> int:
        max_to_left = itertools.accumulate(height, max)
        max_to_right = reversed(list(
            itertools.accumulate(height[::-1], max)))

        return sum(
            min(ml, mr) - h
            for ml, mr, h
            in zip(max_to_left, max_to_right, height))
