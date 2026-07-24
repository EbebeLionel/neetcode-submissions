'''
U
-Given integer array nums and integer k
-return true if:
    -2 distinct indices i and j
    -nums[i] == nums[j]
    -abs(i - j) <= k

    [1,2,3,1], k = 3
     i     j
    abs(3-0) <= 3 == true

    [2,1,2], k = 1
     i   j
     abs(2-0) <= 1 == False

    [2,3,4,2,1,6], k = 4
     i     j

M
-two pointers
P
-if not nums return False
-for loop i in range 0 to second to last elt:
    -for loop j in range len(nums) to i:
        -if nums[i] == nums[j] and abs(i - j) <= k:
            -return True

-return False
IRE
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False