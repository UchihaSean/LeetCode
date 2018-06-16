class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        "len not equal == false"
        if len(s1)+len(s2)!=len(s3): return False
        if s1 == s2 == s3 == "": return True

        "initial"
        f = [[False for j in range(len(s1)+1)] for i in range(len(s3)+1)]
        f[0][0] = True

        for i in range(1,len(s3)+1):
            for j in range(min(i+1,len(s1)+1)):
                "match s1"
                if j>0 and f[i-1][j-1] and s3[i-1] == s1[j-1]:
                    f[i][j] = True
                "match s2"
                if i>j and i-j-1<len(s2) and f[i-1][j] and s3[i-1] == s2[i-j-1]:
                    f[i][j] = True

        return f[len(s3)][len(s1)]





test = Solution()
print test.isInterleave("aabcc","dbbca","aadbbbaccc")