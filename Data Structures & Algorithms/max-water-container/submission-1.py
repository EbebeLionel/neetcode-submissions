'''
U
-Input: array of height
-Output: integer
-Edge case:
    -no height array


[1,7,2,5,4,7,3,6]
   l r

 minHeight = 4

 length = r - l = 4 - 1 = 3
 area = length * minHeight = 4 * 3
 maxArea = 12 or area = 36
M
-Two pointer approach
P
-if not height:
    -return 0

-init l, r to 0, len(height) - 1
init maxArea to 0

while loop as long as l < r:
    set minHeight to min(height[l], height[r])
    area = minHeight * (r - l)
    set maxArea to max(maxArea, area)

    if height[l] < height[r]:
        l += 1

    if height[r] < height[l]:
        r -= 1

    if height[r] == height[l]:
        if (l + 1) != r:
            if height[r - 1] > height[l + 1]:
                r -= 1

            elif height[r - 1] < height[l + 1]:
                l += 1

            else:
                r -= 1

        else:
            l + 1

    return maxArea
IRE

'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return []

        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = minHeight * (r - l)

            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1

            elif heights[r] < heights[l]:
                r -= 1

            elif heights[r] == heights[l]:
                if (l + 1) != r:
                    if heights[r - 1] > heights[l + 1]:
                        r -= 1

                    elif heights[r - 1] < heights[l + 1]:
                        l += 1

                    else:
                        r -= 1

                else:
                    l += 1

        return maxArea