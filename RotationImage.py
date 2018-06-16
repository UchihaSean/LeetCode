class Solution(object):
 def rotate(self, matrix):
    n = len(matrix)
    for l in xrange(n / 2):
        r = n - 1 - l
        for p in xrange(l, r):
            q = n - 1 - p
            cache = matrix[l][p]
            matrix[l][p] = matrix[q][l]
            matrix[q][l] = matrix[r][q]
            matrix[r][q] = matrix[p][r]
            matrix[p][r] = cache







input = [
  [1,2,3],
  [4,5,6],
  [7,8,9] ]


"""
0,0 -- 0,2
0,1 -- 1,2
0,2 -- 2,2
"""
test = Solution()
print test.rotate(input)