from itertools import accumulate


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        workspace = [[-1] * len(l) for l in grid]
        workspace[0] = list(accumulate(grid[0]))
        for i in range(1, len(workspace)):
            workspace[i][0] = workspace[i - 1][0] + grid[i][0]

        for i in range(1, len(workspace)):
            for j in range(1, len(workspace[i])):
                workspace[i][j] = grid[i][j] + min(
                    workspace[i - 1][j], workspace[i][j - 1]
                )
        return workspace[i][j]
