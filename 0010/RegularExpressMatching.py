class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s='a'+s
        p='b'+p
        slen=len(s)
        plen=len(p)
        fmatch = [[False for j in range(plen)] for i in range(slen)]
        fmatch[0][0]=True
        for i in range(slen):
            for j in range(plen):
                if i==0 and j==0: continue
                flag = False
                if i>0 and fmatch[i-1][j]:
                    if j>0 and s[i]==p[j-1] and p[j]=='*': flag=True
                    if j>0 and p[j-1]=='.' and p[j]=='*': flag = True
                if i>0 and j>0 and fmatch[i-1][j-1]:
                    if s[i]==p[j]: flag=True
                    if p[j]=='.': flag=True
                    if j>0 and s[i]==p[j-1] and p[j]=='*':flag=True
                    if j>0 and p[j-1]=='.' and p[j]=='*': flag=True
                if j>1 and fmatch[i][j-2]:
                    if p[j]=='*':flag=True
                fmatch[i][j]=flag
        if fmatch[slen-1][plen-1]: return True
        return False





test = Solution()
print test.isMatch("b","*")