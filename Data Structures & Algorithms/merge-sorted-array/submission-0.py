'''
nums1 = [10,20,20,40,|0,0], m = 4, nums2 = [1,2], n = 2

U
-
MPIRE
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        nums1 = [1,2,10,20,20,40], m = 4, nums2 = [1,2], n = 2
                 ^                                 ^
        pt1 = 2, pt2 = 1, pt = 4
        '''
        pt1, pt2 = m - 1, n - 1
        pt = m + n - 1
        while pt1 >= 0 and pt2 >= 0:
            if nums1[pt1] > nums2[pt2]:
                nums1[pt] = nums1[pt1]
                pt1 -= 1
            else:
                nums1[pt] = nums2[pt2]
                pt2 -= 1

            pt -= 1

        while pt2 >= 0:
            nums1[pt] = nums2[pt2]
            pt2 -= 1
            pt -= 1