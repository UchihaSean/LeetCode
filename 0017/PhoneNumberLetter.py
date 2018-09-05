class Solution(object):
    list_=[]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="": return []
        dict = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.dfs(0,digits,dict,'')
        return self.list_
    def dfs(self,i,digits,dict,letter):
        if i==len(digits):
            self.list_.append(letter)
            return
        for j in range(len(dict[(digits[i])])):
            self.dfs(i+1,digits,dict,letter+dict[digits[i]][j])



test= Solution()
print test.letterCombinations("3")