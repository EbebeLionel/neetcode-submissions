'''
T0 = 0
T1 = 1
T2 = 1
T3 = 2
T4 = 3
T5 = 5
T6 = 8
T7 = 13
T8 = 31
T9 = 48
T10 = 79
T11 = 
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1  or n == 2:
            return 1

        first, second, third = 0,1,1

        while n > 2:
            fourth = first + second + third
            first = second
            second = third
            third = fourth

            n -= 1

        return third