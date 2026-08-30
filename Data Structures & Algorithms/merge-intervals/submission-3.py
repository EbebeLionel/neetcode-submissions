'''
U
-Merge the intervals
-input: 2D array 
-output: 2D array
-Test case:
    -Not intervals

-Sort the array
-Constraint:
    -interval length

[[1,3],[1,5],[6,7]]

res = []

cs, ce = 1, 5

ns, ne = 6, 7

ce >= ns:
    [[1, 5]]
    ce = ne

ce < ns:
    [[1,5]]
    cs, ce = ns, ne

    [[1,5],[6,7]]

M
-intervals

P
-if not intervals return empty []
-sort intervals
-curr_start, curr_end = values of first interval
-for i loop through (1, len(intervals)):
    -next_start
IRE
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])

        res = []
        curr_start, curr_end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i][0], intervals[i][1]

            '''
            [[1,4],[0,4]]
            cs, ce = 1, 4
            ns, ne = , 
            
            ce = 4

            '''

            if curr_end >= next_start:
                curr_end = max(curr_end, next_end)

            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = next_start, next_end

        res.append([curr_start, curr_end])
        return res