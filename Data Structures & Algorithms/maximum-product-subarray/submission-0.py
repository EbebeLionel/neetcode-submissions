'''
nums = [2,4,-3,5]
        ^

    dp = [2,8,8,0]


'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = minVal = maxVal = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                minVal, maxVal = maxVal, minVal

            maxVal = max(curr, maxVal * curr)
            minVal = min(curr, minVal * curr)

            res = max(res, maxVal)

        return res