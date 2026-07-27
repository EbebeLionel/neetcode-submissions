'''
[1,3,4,2,2,4]
 ^

U
-Verify if it's possible to build a square with the matchsticks in the box
-edge case: 
    -no matchsticks

-constraints: a square has 4 sides
M
-backtracking
P
-initialize count var to 0
-find the max val in the array
-define backtrack()
IRE
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]

                    if backtrack(index + 1):
                        return True

                    sides[i] -= matchsticks[index]

                if sides[i] == 0:
                    break

            return False

        return backtrack(0)