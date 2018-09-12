

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        point = []
        for interval in intervals:
            point.append([interval.start, 1])
            point.append([interval.end, -1])

        point.sort()
        rooms = 0
        now = 0
        for x, value in point:
            now+=value
            rooms = max(rooms, now)
        return rooms














test = Solution()

intervals = [Interval(0,30),Interval(15,20),Interval(5,10)]
print(test.minMeetingRooms(intervals))