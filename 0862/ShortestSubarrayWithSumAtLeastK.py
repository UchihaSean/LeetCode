class Solution(object):
    def binary_search(self, stack, t):
        l = 0
        r = len(stack)
        while l + 1 < r:
            mid = (l + r) / 2
            if stack[mid][0] > t:
                r = mid
            else:
                l = mid
        return l

    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        stack = [[0, -1]]
        min_length = len(A) + 1
        pre_sum = 0
        for i in range(len(A)):
            pre_sum += A[i]
            j = self.binary_search(stack, pre_sum - K)
            # print(j, stack[j])
            if pre_sum - stack[j][0] >= K and i - stack[j][1] < min_length:
                min_length = i - stack[j][1]

            while len(stack) > 0 and stack[-1][0] >= pre_sum:
                stack.pop()
            stack.append([pre_sum, i])
        if min_length == len(A) + 1: return -1
        return min_length



