# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [i for i in range(n)]
        while len(stack) > 1:
            l = stack.pop()
            r = stack.pop()
            if knows(l, r):
                stack.append(r)
            else:
                stack.append(l)
        ans = stack[0]
        for i in range(n):
            if i == ans: continue
            if not knows(i, ans) or knows(ans, i): return -1
        return ans
