class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        h, w = len(matrix), len(matrix[0])
        if h == 0 or w == 0: return []
        reach_pac = [[False] * w for i in range(h)]
        reach_at = [[False] * w for i in range(h)]
        for i in range(w): self.dfs(0, i, matrix, reach_pac)
        for i in range(h): self.dfs(i, 0, matrix, reach_pac)
        for i in range(w): self.dfs(h - 1, i, matrix, reach_at)
        for i in range(h): self.dfs(i, w - 1, matrix, reach_at)
        res = []
        for i in range(h):
            for j in range(w):
                if reach_pac[i][j] and reach_at[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, i, j, matrix, target):
        if target[i][j]: return
        target[i][j] = True
        if i > 0 and matrix[i - 1][j] >= matrix[i][j]: self.dfs(i - 1, j, matrix, target)
        if j > 0 and matrix[i][j - 1] >= matrix[i][j]: self.dfs(i, j - 1, matrix, target)
        if i < len(matrix) - 1 and matrix[i + 1][j] >= matrix[i][j]: self.dfs(i + 1, j, matrix, target)
        if j < len(matrix[0]) - 1 and matrix[i][j + 1] >= matrix[i][j]: self.dfs(i, j + 1, matrix, target)


test = Solution()

matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

print(test.pacificAtlantic(matrix))
