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

        n = len(intervals)
        intervals.sort(key = lambda i : i.start)
        s, e = intervals[0].start, intervals[0].end
        
        for i in range(1, n):
            curr_s, curr_e = intervals[i].start, intervals[i].end
            if curr_s >= s and curr_s < e:
                return False
            if curr_e > s and curr_e <= e: 
                return False

            e = curr_e 
                
        return True            