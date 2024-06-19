class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        workspace = [
            [0 if el == 1 else 1 for el in line]
            for line in obstacleGrid
        ]

        for i in range(0, len(workspace)):
            for j in range(0, len(workspace[i])):
                if i == 0 and j == 0:
                    continue
                if workspace[i][j] != 0:
                    up = workspace[i - 1][j] if i > 0 else 0
                    left = workspace[i][j - 1] if j > 0 else 0
                    workspace[i][j] = up + left

        return workspace[-1][-1]
