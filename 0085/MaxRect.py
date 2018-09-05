class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]: return 0


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0: continue
                if j>0 and matrix[i][j-1]>0:
                    matrix[i][j]+= matrix[i][j-1]
        max_rect = 0
        for j in range(len(matrix[0])):
            heights = [matrix[i][j] for i in range(len(matrix))]
            "the number not smaller than index on the left"
            left = self.previous(heights)

            "the number not smaller than index on the right "
            heights.reverse()
            right = self.previous(heights)
            left.reverse()

            for i in range(len(heights)):
                if (left[i]+right[i]+1)*heights[i]>max_rect:
                    max_rect = (left[i]+right[i]+1)*heights[i]
        return max_rect



    def previous(self,heights):
        """
        previous number not smaller than index
        """
        pre = [0 for i in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            # print stack
            left_sum = 0
            while stack!= [] and stack[-1][0]>= heights[i]:
                index, number = stack.pop()
                left_sum += 1+number
            pre[i] = left_sum
            stack.append([heights[i],left_sum])
        return pre






matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]
test = Solution()
print test.maximalRectangle(matrix)