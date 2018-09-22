import heapq
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        one = []
        sum_k = [sum(nums[:k])]
        heapq.heappush(one, [-sum_k[-1], 0])
        for i in range(k, len(nums)):
            sum_k.append(sum_k[-1]+nums[i] - nums[i-k])
            heapq.heappush(one, [-sum_k[-1], i-k+1])

        two = []
        for i in range(len(nums)-k, k-1, -1):
            while one[0][1]+k-1>= i:
                heapq.heappop(one)
            heapq.heappush(two, [one[0][0]-sum_k[i], one[0][1], i])

        three = []
        for i in range(len(nums)-k, 2*k-1, -1):
            while two[0][2]+k-1>=i:
                heapq.heappop(two)
            heapq.heappush(three, [two[0][0]-sum_k[i], two[0][1], two[0][2], i])

        return three[0][1:]




test = Solution()
print test.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
