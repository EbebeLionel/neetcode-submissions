class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: list[int]) -> int:
            rob1, rob2 = 0, 0

            for num in houses:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

        