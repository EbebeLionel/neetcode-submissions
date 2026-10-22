class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return []
            
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = nums[i] + nums[j]
                if total == target and i != j:
                    return [i, j]

