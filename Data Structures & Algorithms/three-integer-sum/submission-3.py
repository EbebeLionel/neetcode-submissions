'''
U
Input: 1D array of nums
Output: 2D array of nums
Edge case:
    nums is empty
        []

Constraints:
    Already given

sort: [-1,0,1,2,-1,-4]
  i l         r
[-4,-1,-1,0,1,2]
        i l r

seen = ()

[[-1,-1,2], [-1,0,1]]
total = 1
M
-three pointer approach

P
if no nums return []

init seen to empty set()
init res to []

for i in range(len(nums) - 2):
    set l, r to i + 1, len(nums) - 1
    while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total == 0:
            if [nums[i], nums[j], nums[r]] not in seen:
                append to res
                add to seen
            
            decrement r by 1

        elif total < 0:
            increment l

        elif total > 0:
            decrement r

return res
IRE
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])

                    r -= 1

                elif total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

        return res