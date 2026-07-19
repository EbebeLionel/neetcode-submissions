class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''my_dict = {}

        #create dictionary
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1

        #loop through dictionary and extract highest freq
        highest = nums[0]
        for key in my_dict.keys():
            if my_dict[key] > my_dict[highest]:
                highest = key

        return highest
        
        [1,1,1,5,5,5,5]
         ^     ^
        '''
        nums = sorted(nums)
        maxCount = 0
        slow, fast = 0, 1
        highest = nums[0]
        while fast < len(nums):
            count = 1
            while fast < len(nums) and nums[slow] == nums[fast]:
                count += 1
                fast += 1
            if count > maxCount:
                highest = nums[slow]
            slow = fast
            fast = slow + 1
            maxCount = max(count, maxCount)

        return highest
