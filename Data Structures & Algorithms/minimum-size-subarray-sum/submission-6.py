'''
U
-Input: 
    -integer target
    -list of nums

-output:
    -integer 
-edge case:
    -no nums

[2,1,5,1,5,3]
M
-
P
-if not nums:
    -return 0
-initialize left to 0
-initialize count to 0
-for right in range from first to last elements in nums:
    -if count < target:
        -increment count with nums[right]

    -else break
if count < target:
    return 0

-while count >= target:
    -decrement count by nums[left]
    -increment left by 1

return right - left + 1
IRE
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or target == 0:
            return 0

        left = 0
        count = 0
        minLen = float('inf')

        for right in range(0, len(nums)):
            count += nums[right]

            
            while count >= target:
                minLen = min(right - left + 1, minLen)
                count -= nums[left]
                left += 1


        if minLen < float('inf'):
            return minLen

        else:
            return 0
