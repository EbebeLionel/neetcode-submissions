'''
[-1,0,2,4,6,8], target = -2
  l 
r
  m

if r < l and m - 1 == -1:
    return 0
if l < r


'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1

            if nums[m] > target:
                r = m - 1

        return l