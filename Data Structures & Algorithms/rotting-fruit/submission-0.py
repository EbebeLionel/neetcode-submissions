'''
U
-[0,1,2] -> [empty cell, fruit, rotten fruit]
-fruits vertically or horizontally adjacent to rotten fruits get rotten after 1 minute
-return how long it takes for all fruits to become rotten
-edge cases:
    -All cells are empty
    -All fruits are not rotten
-constraints:
    -rows and cols <= 10

    [[1,1,0],
     [0,1,1],
     [0,1,2]]

-seen = set()
-explore validation
    -Look at all adjacent cells around the current one
    -explore only when adjacent cells are 1 
    -convert 1s to 2s
    -return -1 if any 1 is left
    -else return time

M
-Graphs BFS
P
-if not grid return 0
-initialize seen set
-initialize time integer
-define helper function bfs(r, c):
    -if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 2:
        -seen.add((r, c))
    -stack = [(r, c)]
    -while stack:
        -row, col = stack.pop()
        -for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            -nr, nc = dr + row, dc + col
            -if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                -time += 1
                -seen.add((nr, nc))
                -grid[nr][nc] == 2
                -bfs(nr, nc)
                -stack.append((nr, nc))


-find rotten fruits:
-for r
I

RE
'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # 1. Collect all initial rotten oranges AND count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Edge Case: If there are no fresh oranges to rot, 0 minutes have passed
        if fresh_count == 0:
            return 0

        minutes = 0

        # 2. Multi-Source BFS
        while queue and fresh_count > 0:
            minutes += 1
            
            # Process all oranges rotten at the CURRENT minute level
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Convert fresh to rotten
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))

        # 3. If any fresh oranges remain unreachable, return -1
        return minutes if fresh_count == 0 else -1