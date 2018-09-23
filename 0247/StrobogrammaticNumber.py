class Solution(object):
    def dfs(self, i, n, now):
        if n % 2 == 1 and i == n / 2 + 1:
            self.ans.extend([now + '1', now + '0', now + '8'])
            return None
        if n % 2 == 0 and i == n / 2 + 1:
            self.ans.append(now)
            return None
        for c in '1689':
            self.dfs(i + 1, n, now + c)
        if i != 1:
            self.dfs(i + 1, n, now + '0')

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(1, n, "")
        # print(self.ans)
        for i in range(len(self.ans)):
            if n % 2 == 0:
                now = len(self.ans[i]) - 1
            else:
                now = len(self.ans[i]) - 2
            # print(i,now)
            for j in range(now, -1, -1):
                if self.ans[i][j] in '018':
                    self.ans[i] += self.ans[i][j]
                if self.ans[i][j] == '6':
                    self.ans[i] += '9'
                if self.ans[i][j] == '9':
                    self.ans[i] += '6'
        return self.ans


test = Solution()
print test.findStrobogrammatic(2)