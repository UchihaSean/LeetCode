class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        def dfs(t,now):
            if t==len(lis):
                sol.append(now)
                return None
            for i in range(dic[lis[t]]+1):
                dfs(t+1,now+ [lis[t] for _ in range(i)])


        dic = {}
        lis = []
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                lis.append(num)
                dic[num] = 1

        sol = []

        dfs(0,[])

        return sol



test = Solution()
print test.subsetsWithDup([1,1])