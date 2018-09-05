# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []:
            return [newInterval]
        left = -1
        right = -1
        for i,interval in enumerate(intervals):
            if interval.end>=newInterval.start:
                left = i
                break
        for i in range(len(intervals)-1,-1,-1):
            if intervals[i].start<= newInterval.end:
                right = i
                break


        if left == -1:
            intervals.append(newInterval)
            return intervals
        if right == -1:
            intervals.insert(0,newInterval)
            return intervals

        if left>right:
            intervals.insert(left,newInterval)
            return intervals

        if left == right:
            intervals[left] = Interval(min(intervals[left].start,newInterval.start),max(intervals[left].end,newInterval.end))
            return intervals

        if left<right:
            newIntervals = intervals[:left]+intervals[right+1:]
            newIntervals.insert(left,Interval(min(intervals[left].start,newInterval.start),max(intervals[right].end,newInterval.end)))
            return newIntervals

        return None
