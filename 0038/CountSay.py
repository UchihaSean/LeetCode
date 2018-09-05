class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "11"
        if n==0: return  ""
        if n==1: return "1"
        for i in range(n-2):
            repeat = 1
            new_s = ""
            for j in range(1,len(s)):
                if s[j]==s[j-1]:
                    repeat+=1
                else:
                    new_s=new_s+str(repeat)+s[j-1]
                    repeat=1
            new_s+=str(repeat)+s[len(s)-1]
            s = new_s
        return s



test = Solution()
print test.countAndSay(100)