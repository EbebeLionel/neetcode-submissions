'''
U
-Input: array of integers, single integer
-output: single integer
-Edge case:
    -no nums

-Constraints
M
P
-
IRE'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                # Check if target lies within the left sorted half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target lies within the right sorted half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1