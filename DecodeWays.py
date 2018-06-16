class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s)<1: return 0
        if len(s)==1:
            if s == '0': return 0
            return 1
        # end with one letter
        f = [0 for _ in range(len(s))]

        # end with two letters
        g = [0 for _ in range(len(s))]

        if int(s[0])!=0: f[0] = 1
        if 0<int(s[:2])<=26 and int(s[0])!=0: g[1] = 1

        for i in range(1,len(s)):
            if int(s[i])!=0:
                f[i] = f[i-1]+g[i-1]
            if i>1 and 0<int(s[i-1:i+1])<=26 and int(s[i-1])!=0:
                g[i] = f[i-2]+g[i-2]

        return g[len(s)-1]+f[len(s)-1]




test = Solution()
print test.numDecodings("01")