'''

'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #if not intervals:
           # return []

        intervals.append(newInterval)

        intervals.sort(key=lambda x:x[0])

        curr_start, curr_end = intervals[0][0], intervals[0][1]
        res = []

        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i][0], intervals[i][1]

            if curr_end >= next_start:
                curr_end = max(curr_end, next_end)

            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = next_start, next_end

        res.append([curr_start, curr_end])
        return res