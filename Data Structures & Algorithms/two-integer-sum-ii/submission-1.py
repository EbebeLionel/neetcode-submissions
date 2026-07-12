'''
U
numbers = [1,2,3,4], target = 3

[1,2,3,4], total = 3
 ^ ^

M
-Two pointers
P
-if not numbers return []
-initliaze 2 pointers l and r to 0 and len(numbers) - 1 respectively
-while l < r:
    -total = sum of numbers[l] and numbers[r]
    -if total = target number we return an array of l and r
    -elif total is not equal to target number:
        -if total exceeds target we decrement r
        -elif total is less than target we increment l

-return an empty array
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [(l + 1), (r + 1)]
            elif total != target:
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1

        return []