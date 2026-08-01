from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # 1. Add all treasure chests (0) to the queue as starting sources
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # 2. Multi-source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                # Check boundary bounds and if the cell is unvisited land (INF = 2147483647)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    # Set distance to current distance + 1
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))