'''
[1,2,3,4,5,6,7,8] , k = 2
[8] + [1,2,3,4,5,6,7]
[7] + [8,1,2,3,4,5,6,]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums[:] = nums[-k:] + nums[:-k]

