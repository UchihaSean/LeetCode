class Solution(object):
    def dfs(self, matrix, x, y, length, last):
        if x < 0 or y < 0 or x == len(matrix) or y == len(matrix[0]):
            return 0
        if matrix[x][y] <= last:
            return 0
        if (x, y) in length:
            return length[(x, y)]

        dir = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        res =1+ max(self.dfs(matrix, a, b, length, matrix[x][y] ) for a,b in dir)
        length[(x,y)] = res
        return res

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        max_length = 0
        length = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_length = max(max_length, self.dfs(matrix, i, j, length, matrix[i][j] - 1))
        return max_length


test = Solution()
nums = [[7, 7, 5], [2, 4, 6], [8, 2, 0]]
print(test.longestIncreasingPath(nums))
