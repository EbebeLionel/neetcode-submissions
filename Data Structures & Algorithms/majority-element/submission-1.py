class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}

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