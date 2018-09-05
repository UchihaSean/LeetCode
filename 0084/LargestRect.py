
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        "the number not smaller than index on the left"
        left = self.previous(heights)

        "the number not smaller than index on the right "
        heights.reverse()
        right = self.previous(heights)
        left.reverse()

        "max rectangle area"
        max_rect = 0
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







test = Solution()
print test.largestRectangleArea([2,2,4,6,2,3])