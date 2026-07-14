class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current):
            if index == len(nums):
                return current
            include = backtrack(index + 1, current ^ nums[index])
            exclude = backtrack(index + 1, current)

            return include + exclude
        return backtrack(0, 0)