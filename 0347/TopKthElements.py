import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        ans = []
        for num in dic:
            if len(ans) < k:
                heapq.heappush(ans, [dic[num], num])
            else:
                item = heapq.heappop(ans)
                if dic[num] > item[0]:
                    item = [dic[num], num]
                heapq.heappush(ans, item)
        return [item[1] for item in ans]

