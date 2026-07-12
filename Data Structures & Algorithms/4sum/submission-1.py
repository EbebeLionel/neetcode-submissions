'''
U
-input: Array of size n
-output: return an array of unique quadruplets that sum up to target
-Array is unsorted
-Edge cases: Array might be empty
-Constraints: 1 <= nums.length <= 200
                -1,000,000,000 <= nums[i] <= 1,000,000,000
                -1,000,000,000 <= target <= 1,000,000,000
[3,2,3,-3,1,0] -> [-3,0,1,2,3,3] t = 3
                    i   l r   j

                    [-3,0,3,3], [-3,1,2,3]

[1,-1,1,-1,1,-1] -> [-1,-1,-1,1,1,1], t = 2
                      i       l r l

                    []  
M
-4 pointers
P
-if not nums return empty array
-sort nums
-initialize empty array, res
-for i in range len(n):
    -if nums i > t:
        return empty array

    -if i > 0 and nums[i] == nums[i - 1]:
        -skip this loop(continue) to avoid duplicates

    -initialize variables l = i + 1, j = n - 1, r = j - 1
    -while l < r:
        -total = sum of nums at i,j,l,r
        -if total == target:
            -res.append(all 4 elts)
            -while l < r and nums[l] == nums[l + 1]:
                -increment l
            -while l < r and nums[r] == nums[r - 1]:
                -decrement r

            -increment l
            -decrement r

        -elif total < t:
            -increment l
        -else:
            -decrement r

    j -= 1

return res
        
I
-inProgress
RE
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n - 3):
            #if nums[i] > t then no combination of numbersd will sum up to the target so we skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second anchor loop
            for j in range(i + 1, n - 2):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Classic two-pointer window
                l = j + 1
                r = n - 1

                while l < r:
                    total = nums[i] + nums[l] + nums[r] + nums[j]
                    if total == target:
                        res.append([nums[i], nums[l], nums[r], nums[j]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1


        return res