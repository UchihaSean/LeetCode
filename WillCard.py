class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        "Prevent empty strings"
        s = "a"+s
        p = "a"+p

        "Initial match list"
        match = [[False for j in range(len(p))] for i in range(len(s))]
        "First one match"
        match[0][0] = True
        for i in range(len(s)):
            for j in range(len(p)):
                "one char match, a ? *"
                if i>0 and j>0 and match[i-1][j-1] and (s[i]==p[j] or p[j]=="?" or p[j]=="*"):
                    match[i][j] = True
                "several chars match, *"
                if p[j] == "*":
                    if j>0 and match[i][j-1]: match[i][j] = True
                    if i>0 and match[i-1][j]: match[i][j] = True

        return match[len(s)-1][len(p)-1]




test = Solution()
print test.isMatch("","*")