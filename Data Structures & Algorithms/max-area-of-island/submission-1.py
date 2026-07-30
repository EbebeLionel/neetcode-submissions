'''
U
-Find the max Area of an island
-grid[i][j] == "1" is land
-grid[i][j] == "0" is water
-Edge case:
    -No land
    -No grid at all

-Constraints

-handle the edge case
-Use maxArea variable to update anytime we find a higher area than the prev one
-instead of using nr and nc, use the modulo of nr and nc
-since we are using the modulo of neighboring rows and columns we do not need to bother about bounds
M
-graphs
P
-if not grid return 0
-initialize visit set
-initialize maxArea
-define explore function with parameters r and c
    -stack = [(r, c)]
    -for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        row, col = stack.pop()
        nr, nc = ((dr + row) % len(grid)), ((dc + col) % len(grid[0]))
        if (nr, nc) not in visit:
            area += 1
            visit.add((nr, nc))
            stack.append((nr, nc))

-for i in range(len(grid)):
    -for j in range(len(grid[0])):
        -if grid[i][j] == "1" and (i, j) not in visit:
            -area += 1
            -visit.add((i, j))
            -explore((i, j))
            -maxArea = max(area, MaxArea)
IRE
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visit = set()
        maxArea = 0

        def explore(r, c):
            stack = [(r, c)]
            visit.add((r, c))
            area = 0
            while stack:
                row, col = stack.pop()
                area += 1
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = dr + row, dc + col
                    if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        visit.add((nr, nc))
                        stack.append((nr, nc))

            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, explore(r, c))

        return maxArea


