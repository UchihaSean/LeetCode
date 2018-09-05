class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        left = right = n
        now = ""
        self.generate(left,right,ans,now)
        return ans
    def generate(self,left,right,ans,now):
        if left>right: return
        if left==right == 0:
            ans.append(now)
        if left>0:
            self.generate(left-1,right,ans,now+"(")
        if right>0:
            self.generate(left,right-1,ans,now+")")



test = Solution()
print test.generateParenthesis(3)