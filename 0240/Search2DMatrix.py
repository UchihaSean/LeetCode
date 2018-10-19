class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]]: return False
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[0])
            while l + 1 < r:
                mid = (l + r) / 2
                if matrix[i][mid] <= target:
                    l = mid
                else:
                    r = mid
            if matrix[i][l] == target: return True
        return False
