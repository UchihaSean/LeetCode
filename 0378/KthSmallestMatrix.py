import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        num = []
        ans = None
        for i in range(len(matrix)):
            heapq.heappush(num, [matrix[i][0], i, 0])
        for i in range(k):
            ans, x, y = heapq.heappop(num)
            if y + 1 < len(matrix[0]):
                heapq.heappush(num, [matrix[x][y + 1], x, y + 1])
        return ans

