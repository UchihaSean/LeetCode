class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Special Case
        if len(matrix)==0 or len(matrix[0])==0: return False


        # Search the row of matrix for target
        row = 0
        while row<len(matrix) and matrix[row][0]<=target: row+=1

        # Smaller than the first element == Not exist
        if row == 0: return False

        # The row need to be searched
        search_list = matrix[row-1]

        l = 0
        r = len(search_list)-1

        # Divide search
        while l<r:
            mid = (l+r)/2
            if search_list[mid]<target:
                l = mid +1
            else:
                r = mid

        if search_list[r] == target: return True

        return False



test = Solution()
print test.searchMatrix([[1]],1)