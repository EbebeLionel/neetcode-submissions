'''
1 to 4
[1,4,3,2], h = 9
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            m = (l + r) // 2

            hours_needed = sum((p + m - 1) // m for p in piles)

            if hours_needed <= h:
                ans = m
                r = m - 1

            else:
                l = m + 1

        return ans