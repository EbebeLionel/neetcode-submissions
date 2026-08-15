class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1]:
            return 0

        row = [0] * n
        row[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                elif j > 0:
                    row[j] += row[j - 1]

        return row[-1]