class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        minus = False
        if n<0:
            minus = True
            n = -n
        ans = 1
        while n>0:
            if n % 2 == 1:
                ans *= x

            n = n >> 1
            x = x * x
        if minus: return 1.0/ans
        return ans


"""
1010
"""
test = Solution()
print test.myPow(34,-3)