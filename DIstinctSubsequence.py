class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        "initial"
        f = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        f[0][0] = 1

        for i in range(1,len(s)+1):
            for j in range(len(t)+1):
                "not add chars in t"
                f[i][j] += f[i-1][j]
                "add one char in t"
                if j>0 and s[i-1] == t[j-1]:
                    f[i][j] += f[i-1][j-1]

        return f[len(s)][len(t)]





test = Solution()
print test.numDistinct("","")