'''
U
-Input: array of nums
-Output: Array of nums
-Edge cases:
    -Nums is empty

-Constraints:
    -Already given

[1,2,4,6]

res = [1,1,2,4]

res[i] = pref
           * 
pref *= nums[i]

suffix = 1
res[i] *= suffix
suffix *= nums[i] = 6
[48,24,12,8]
M
-Prefix/Suffix
P
-Handle edge case
-create res array of length 
-init prefix to 1
-fpr loop through nums:
    -set res[i] to prefix
    -Increment prefix to prefix *= nums[i]

-init suffix = 1
-for loop through nums:
    -increment res[i] by * suffix
    -increment prefix to * nums[i]

-return res
IRE
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res