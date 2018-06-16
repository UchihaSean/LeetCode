# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        "Special Case"
        if intervals == []: return []

        "Store merged intervals"
        merged_intervals = []
        "Sort intervals with start"
        intervals = sorted(intervals,key=lambda s:s.start)

        "First range"
        left, right = intervals[0].start, intervals[0].end

        "Cycle to merge all possible"
        for i in range(1,len(intervals)):
            "If overlap"
            if intervals[i].start<= right:
                right = max(right,intervals[i].end)
            else:
                "Not overlap, add this range and change to another range"
                merged_intervals.append(Interval(left,right))
                left, right = intervals[i].start, intervals[i].end

        "add the last range"
        merged_intervals.append(Interval(left,right))

        return merged_intervals

