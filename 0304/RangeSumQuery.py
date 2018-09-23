class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return None
        self.lsum = []
        for i in range(len(matrix)):
            self.lsum.append([matrix[i][0]])
            for j in range(1, len(matrix[0])):
                self.lsum[i].append(self.lsum[i][-1] + matrix[i][j])
        self.lusum = [self.lsum[0]]
        for i in range(1, len(matrix)):
            self.lusum.append([])
            for j in range(len(matrix[0])):
                self.lusum[i].append(self.lsum[i][j] + self.lusum[i - 1][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        ans += self.lusum[row2][col2]
        if row1 > 0:
            ans -= self.lusum[row1 - 1][col2]
        if col1 > 0:
            ans -= self.lusum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            ans += self.lusum[row1 - 1][col1 - 1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)