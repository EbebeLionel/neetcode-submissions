"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.end)

        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        start_pt = 0
        end_pt = 0
        max_rooms = 0
        active_rooms = 0

        while start_pt < len(intervals):
            if starts[start_pt] < ends[end_pt]:
                active_rooms += 1
                max_rooms = max(max_rooms, active_rooms)
                start_pt += 1

            else:
                active_rooms -= 1
                end_pt += 1

        return max_rooms