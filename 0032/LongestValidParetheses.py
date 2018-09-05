class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        f = [0 for i in range(len(s)+1)]
        max_len = 0
        for i in range(2,len(s)+1):

            if s[i-1] == ")" and s[i-2]=="(" and f[i]<f[i-2]+2:
                f[i]=f[i-2]+2

            if i>=f[i-1]+2 and s[i-1] ==")" and s[i-2]==")" and s[i-f[i-1]-2]=="(" and f[i]<f[i-1]+2+f[i-f[i-1]-2]:
                f[i]=f[i-1]+f[i-f[i-1]-2]+2

            if f[i]>max_len:
                max_len=f[i]



        return max_len







test = Solution()
print test.longestValidParentheses("(()))())(")