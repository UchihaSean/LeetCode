class Solution(object):
    def bfs(self, x, y, grid, dis):
        l = -1
        q = [[x, y, 0]]
        dis[x][y] = 0
        while l < len(q)-1:
            l += 1
            x, y, cur = q[l]
            if x>0 and grid[x-1][y]==0 and dis[x-1][y]==-1:
                dis[x-1][y] = cur+1
                q.append([x-1, y, cur+1])
            if y>0 and grid[x][y-1]==0 and dis[x][y-1]==-1:
                dis[x][y-1] = cur+1
                q.append([x, y-1, cur+1])
            if x<len(grid)-1 and grid[x+1][y]==0 and dis[x+1][y]==-1:
                dis[x+1][y] = cur+1
                q.append([x+1, y, cur+1])
            if y<len(grid[0])-1 and grid[x][y+1]==0 and dis[x][y+1]==-1:
                dis[x][y+1] = cur+1
                q.append([x, y+1, cur+1])


    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dis = [[-1 for y in range(len(grid[0]))] for x in range(len(grid))]
                    self.bfs(i, j, grid, dis)
                    # print(i, j)
                    # print(dis)
                    for x in range(len(grid)):
                        for y in range(len(grid[0])):
                            if dis[x][y] == -1:
                                ans[x][y] = -2
                            else:
                                if ans[x][y] != -2:
                                    ans[x][y] += dis[x][y]
        # print(ans)
        min_dis = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ans[i][j] != -2 and grid[i][j] == 0:
                    if min_dis == -1:
                        min_dis = ans[i][j]
                    else:
                        if min_dis > ans[i][j]:
                            min_dis = ans[i][j]
        return min_dis if min_dis != -1 else -1


test = Solution()
print test.shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
