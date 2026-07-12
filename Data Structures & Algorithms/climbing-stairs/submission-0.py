'''

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2

        while n > 2:
            third = first + second
            first = second
            second = third
            n -= 1

        return second
