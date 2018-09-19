import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]

test = Solution()
print test.findKthLargest([3,2,1,5,6,4],2)

