'''
U
-Input: 2x2 matrix board
-Output: Boolean
-Edge case:
    -no board
    -constraints
for loop?

#Check if rows have duplicates
for i in range(board):
    seen = set()
    for j in range(board):
        if nums[j] in seen:
            return False
        seen.add(nums[j])
#Check if columns have duplicates
for i in range(board):
    seen = set()
    for j in range(board):
        if nums[i] in seen:
            return False
        seen.add(nums)

#Check if boxes have duplicates
lowerbound = 0
upperbound = 3
while upperbound < board:
    for i in range(lowerbound, upperbound):
        seen = set()
        for j in range(lowerbound, upperbound):
            if nums[j] in seen:
                return False
            seen.add(nums[j])
    lowerbound += 3
    upperbound += 3
    
return True


return True
M
Array
PIRE
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        #Check if rows have duplicates
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] != "." and board[i][j] in seen:
                    return False
                seen.add(board[i][j])
                print(seen)

        #Check if columns have duplicates
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        #Check if boxes have duplicates
        for row_start in range(0, len(board), 3):
            for col_start in range(0, len(board), 3):
                seen = set()
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] != ".":
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
                
        return True

        '''
        [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]
        '''
