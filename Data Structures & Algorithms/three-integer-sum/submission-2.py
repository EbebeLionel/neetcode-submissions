'''
U
-[-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
                       l         i r   

   [[-1,0,1],[-1,2,-1]]
M
-three pointer problem
P
-if not nums return an empty array
-sort the array
-initialize an empty array res
-for loop through array starting from 1 to the end:
    -initialize l and r equal to 0 and len(nums) - 1 respectively
    -while i is less than r and i is greater than r:
        -total = sum of nums[l], nums[i], and nums[r]
        -if total equals 0:
            -append [nums[l], nums[i], nums[l]] to res
        -elif total < 0:
            -increment l
        -elif total > 0:
            -decrement r

return res

IRE
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Optimization: Since it's sorted, if the anchor is > 0, 
            # no three positive numbers can ever sum to 0. Stop early.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the anchor element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Move pointers past duplicates for 'l' and 'r'
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    # Shift both inward to find new combinations
                    l += 1
                    r -= 1
                    
                elif total < 0:
                    l += 1  # Sum is too small, make it larger
                else:
                    r -= 1  # Sum is too big, make it smaller
                    
        return res

                
            