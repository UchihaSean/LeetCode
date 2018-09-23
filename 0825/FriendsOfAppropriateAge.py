class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        age_sum = [0 for _ in range(121)]
        for age in ages:
            age_sum[age] += 1
        for age in range(1, 121):
            age_sum[age] += age_sum[age - 1]
        requests = 0

        for age in ages:
            x = int(0.5 * age + 8)
            y = age
            if age < 100:
                y = min(y, 100)
            requests += age_sum[y] - age_sum[x - 1] if y >= x else 0
            if age >= x and age <= y:
                requests -= 1
        return requests
