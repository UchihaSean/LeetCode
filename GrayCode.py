class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # Special Case
        if n<1: return [0]

        sol = [0,1]

        for i in range(n-1):
            revese_sol = list(reversed(sol))
            revese_sol = [(1<<(i+1))+revese_sol[j] for j in range(len(sol))]
            sol.extend(revese_sol)

        return sol





test = Solution()
print test.grayCode(20)