import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        "Initial"
        dict = {}
        for i in range(len(t)):
            if t[i] not in dict:
                dict[t[i]] = 1
            else:
                dict[t[i]]+=1

        "how much char need to match"
        missing = len(t)

        l = r = -1
        ll = 0
        "Cycle every char"
        for i in range(len(s)):
            "if match one char"
            if s[i] in dict and dict[s[i]]>0: missing-=1
            " dict[c]<0 means enough c"
            if s[i] not in dict:
                dict[s[i]] =-1
            else:
                dict[s[i]] -=1


            "All matched"
            if missing<=0:
                while ll<i and dict[s[ll]]<0:
                    dict[s[ll]]+=1
                    ll+=1
                if l == -1 or i-ll<=r-l:
                    l,r = ll, i

        return s[l:r+1]






test = Solution()
print test.minWindow("ab","a")