'''
[1,7,2,5,4,7,3,6]

U
-Given an array heights
-heights[i] represents height of bar
-input: array of heights
-output: integer

[1,7,2,5,4,7,3,6]
         l r

 
 maxArea = 0
 minHeight = (4, 7) = 4
 area = (r - l) * minHeight = 1 * 4 = 4 
 maxArea = (area, maxArea) = (4, 36) = 36
M
-two pointer
P
-if not heights return 0 
-initialize 2 pointers l, r = 0, len(heights) - 1
-initialize maxArea = 0
-while l < r:
    -minHeight = min(heights[l], heights[r])
    -area = (r - l) * minHeight
    -maxArea = max(area, maxArea)
    -if heights[l] < heights[r] or heights[l] == heights[r]:
        -increment l
    -elif heights[l] > heights[r]:
        -decrement r

-return maxArea
I
-In progress
RE
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = (r - l) * minHeight
            maxArea = max(area, maxArea)
            if heights[l] < heights[r] or heights[l] == heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return maxArea