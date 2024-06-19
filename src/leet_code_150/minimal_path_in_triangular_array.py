class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        calculated_level = triangle[-1]

        for level in reversed(triangle[:-1]):
            calculated_level = [
                level[i] + min(calculated_level[i], calculated_level[i + 1])
                for i in range(len(level))]

        return calculated_level[0]
