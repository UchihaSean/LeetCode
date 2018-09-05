class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=False
        if x<0: flag=True
        x=abs(x)
        y=0
        while x>0:
            y=y*10+x % 10
            x=x/10

        if y>2**31: return 0
        if flag: y=-y
        return y




test= Solution()

print test.reverse(-120)