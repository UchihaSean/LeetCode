class Solution(object):
    def dfs(self, t, c, graph):
        if self.color[t] != -1:
            if self.color[t] != c:
                return False
            return True
        self.color[t] = c
        for next in graph[t]:
            if not self.dfs(next, 1 - c, graph):
                return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.color = [-1 for _ in range(len(graph))]

        for i in range(len(graph)):
            if self.color[i] == -1 and not self.dfs(i, 1, graph):
                return False
        return True
