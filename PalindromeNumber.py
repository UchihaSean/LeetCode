class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False
        power=0
        while True:
            if 10**power>x:break
            power+=1
        power-=1
        while True:
            if x==0: break
            if x % 10 != x / (10**power): return False
            x = x % (10**power) / 10
            power-=2
        return True


test = Solution()
print test.isPalindrome(-123221)