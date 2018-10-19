import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        max_lis = []
        ans = []
        for i in range(k):
            heapq.heappush(max_lis, [-nums[i], i])
        ans.append(-max_lis[0][0])
        for i in range(k, len(nums)):
            while len(max_lis) > 0 and max_lis[0][1] + k <= i:
                heapq.heappop(max_lis)
            heapq.heappush(max_lis, [-nums[i], i])
            ans.append(-max_lis[0][0])
        return ans
