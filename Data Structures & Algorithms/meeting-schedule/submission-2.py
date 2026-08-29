"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        
        currStart = intervals[0].start
        currEnd = intervals[0].end

        for i in range(1, len(intervals)):
            nextStart, nextEnd = intervals[i].start,intervals[i].end
            if currEnd > nextStart:
                return False

            currStart, currEnd = nextStart, nextEnd

        return True