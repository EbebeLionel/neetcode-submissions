class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d_two = 0
        d_one = 0

        for i in range(2, len(cost) + 1):
            curr = min(d_one + cost[i - 1], d_two + cost[i - 2])

            d_two = d_one
            d_one = curr

        return d_one