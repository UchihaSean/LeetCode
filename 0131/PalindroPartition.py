class Solution(object):
    def dfs(self, s, path, res):
        if s == "":
            res.append(path)
            return None
        for i in range(1, len(s) + 1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def isPar(self, s):
        return s == s[::-1]



test = Solution()
print test.partition("aab")
