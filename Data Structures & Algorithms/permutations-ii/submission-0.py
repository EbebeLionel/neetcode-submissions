'''
[1,1,2]

mark a number using 
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                curr.append(nums[i])
                used[i] = True

                backtrack(curr)

                used[i] = False
                curr.pop()

        backtrack([])
        return res