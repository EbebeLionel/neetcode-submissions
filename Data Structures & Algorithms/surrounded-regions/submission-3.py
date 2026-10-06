'''
U

MPIRE
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        seen = set()

        def explore(r, c):
            track = [(r, c)]

            stack = [(r, c)]

            while stack:
                row, col = stack.pop()
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and board[nr][nc] == 'O':
                        seen.add((nr, nc))
                        track.append((nr, nc))
                        stack.append((nr, nc))

            for ro, co in track:
                if (ro + 1) >= rows or (co + 1) >= cols or (ro - 1) < 0 or (co - 1) < 0:
                    return
                
            
            for ro, co in track:
                board[ro][co] = 'X'

            return


        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and board[r][c] == 'O':
                    seen.add((r,c))
                    explore(r, c)

        return