class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        "special case"
        if s=="": return 0

        "initial"
        palindrome = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            "aabaa type of palindrome"
            for j in range(min(i+1,len(s)-i)):
                if s[i+j] != s[i-j]: break
                palindrome[i-j][i+j] = True
            "aabb type of palindrome"
            for j in range(min(i+1,len(s)-i-1)):
                if s[i+j+1] != s[i-j]: break
                palindrome[i-j][i+j+1] = True

        "how many cut need"
        f = [i+1 for _ in range(len(s))]

        for i in range(len(s)):
            "whole string is palindrome"
            if palindrome[0][i]:
                f[i] = 1
                continue
            "dynamic program"
            for j in range(i):
                if f[i]>f[j]+1 and palindrome[j+1][i]:
                    f[i] = f[j]+1

        return f[len(s)-1] -1






test = Solution()
print test.minCut("ab")