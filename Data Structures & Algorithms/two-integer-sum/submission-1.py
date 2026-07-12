'''
[3,4,5,6]

U
-Given an array, return array of indices whose elements sum up to target
-edge case: array is empty
-constraints: only one pair exists

[3,4,5,6], t = 7
 ^

 7 - 3 = 4

M
-Array & Hashing
P
-if array is empty return an empty array
-for loop through array
    -set complement equal to target minus nums[i]
    -if complement in nums:
        -return array of i and index of complement

-if we do not find any complement, return empty array
I
-
RE
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []