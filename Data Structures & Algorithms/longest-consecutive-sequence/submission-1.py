'''
U
-Input: array of nums
-Output: Integer
-Edge case:
    -No array
    -Array empty
-Sort out the array
-[2,3,4,4,5,10,20]
-[0,1,1,2,3,4,5,6]

i - 1 -> i
count = 1

nums[i - 1] == nums[i] - 1
    count += 1
nums[i - 1] == nums[i]

return count
Utilize a for loop but start looping from 2nd element
MPIRE
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        count = 1
        maxCount = 0

        print(sorted([9,1,4,7,3,-1,0,5,8,-1,6]))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1

            elif nums[i] == nums[i - 1]:
                continue

            else:
                maxCount = max(maxCount, count)
                count = 1

        return max(maxCount, count)