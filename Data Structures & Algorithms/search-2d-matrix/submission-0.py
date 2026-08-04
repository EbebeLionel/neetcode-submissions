'''
[[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
  l              m                 r

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                left, right = 0, len(matrix[m]) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if matrix[m][mid] == target:
                        return True

                    if matrix[m][mid] < target:
                        left = mid + 1

                    if matrix[m][mid] > target:
                        right = mid - 1

                return False

            if matrix[m][0] > target:
                r = m - 1

            if matrix[m][-1] < target:
                l = m + 1

        return False