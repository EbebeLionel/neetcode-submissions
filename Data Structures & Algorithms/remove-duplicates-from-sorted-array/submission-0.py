'''
U
-[1,1,2,3,4]
M
-Two pointers
P
-initialize an empty array, res
-initialize 2 pointers, p1 and p2
-while p2 is less than len(nums)
    -if p1 == p2:
        -if nums[p1] == nums[p2]
            -append to res
            -increment p2
    -elif p1 != p2:
        -if nums[p1] == nums[p2]:
            -increment p2
        -elif nums[p1] != nums[p2]:
            -set p1 to p2
            
return res
 

p1, p2 = 0, 1
 
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        idx = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1

        return idx
