class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        numbers = set([int(s) for s in time if s != ":"])
        if len(numbers)==1: return time
        x, y = [int(s) for s in time.split(":")]
        # print(x, y)

        hours = [a * 10 + b for a in numbers for b in numbers if a * 10 + b < 24]
        minutes = [a * 10 + b for a in numbers for b in numbers if a * 10 + b < 60]
        min_length = 999999
        next_time = ""

        # iterate each time
        for hour in hours:
            for minute in minutes:
                # calculate length
                length = (3600 * 24 + hour * 3600 + minute * 60 - x * 3600 - y * 60) % (3600 * 24)
                if length == 0: continue
                # choose the closest time
                if length < min_length:
                    min_length = length
                    next_time = ""
                    if hour < 10: next_time = "0"
                    next_time += str(hour) + ":"
                    if minute < 10: next_time += "0"
                    next_time += str(minute)

        return next_time


test = Solution()
print(test.nextClosestTime("00:00"))
