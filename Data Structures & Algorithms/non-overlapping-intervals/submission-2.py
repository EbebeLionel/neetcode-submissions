'''
U
-Given an array of intervals, return how many intervals need to be removed to make it non-overlapping
-Input: 2D array of intervals
-output: integer of # of intervals to remove
-Edge case:
    -no intervals
-Constraints
    -?

make two sorted arrays: starts and ends
starts is an array of all starting bounds
ends is an array of all ending bounds

initialize variables
-start_pt = 0
-end_pt = 0
-max_intervals = 0
-overlaps = 0

[[1,2],[1,4],[2,4]]

starts = [1,1,2]
ends = [2,4,4]

sp = 0, ep = 0, maxInt = 0, overlaps = 0



M
-intervals
P
make two sorted arrays: starts and ends
starts is an array of all starting bounds
ends is an array of all ending bounds

initialize variables
-start_pt = 0
-end_pt = 0
-max_intervals = 0
-overlaps = 0


IRE
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res