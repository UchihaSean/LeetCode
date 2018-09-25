class Solution(object):
    def get_father(self, t, father):
        if father[t] == t: return t
        father[t] = self.get_father(father[t], father)
        return father[t]

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        father = [i for i in range(m * n)]
        island = [0 for _ in range(m * n)]
        ans = []
        for x, y in positions:
            island[x * n + y] = 1
            up, down, left, right = -1, -1, -1, -1
            if x > 0 and island[(x - 1) * n + y] == 1: up = self.get_father((x - 1) * n + y, father)
            if y > 0 and island[x * n + y - 1] == 1: left = self.get_father(x * n + y - 1, father)
            if x < m - 1 and island[(x + 1) * n + y] == 1: down = self.get_father((x + 1) * n + y, father)
            if y < n - 1 and island[x * n + y + 1] == 1: right = self.get_father(x * n + y + 1, father)
            center = self.get_father(x * n + y, father)
            group = set([-1, up, down, left, right])
            if len(ans) == 0:
                ans.append(1)
            else:
                # print(ans, len(group))
                ans.append(ans[-1] + (2 - len(group)))
            for point in [up, down, left, right]:
                if point != -1:
                    father[point] = center
        return ans

