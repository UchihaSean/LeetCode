class Solution(object):

    def dfs(self,grid, x, y):
        grid[x][y] = '0'
        if x+1<len(grid) and grid[x+1][y]=='1':
            self.dfs(grid, x+1, y)

        if x>0 and grid[x-1][y] == '1':
            self.dfs(grid, x-1, y)

        if y+1<len(grid[0]) and grid[x][y+1]=='1':
            self.dfs(grid, x, y+1)

        if y>0 and grid[x][y-1]=='1':
            self.dfs(grid, x, y-1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid: return 0
        islandNum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i, j)
                    islandNum += 1

        return islandNum


test = Solution()
island = [
    ['1','1','0'],
    ['0','1','1'],
    ['1','0','0']
]
print test.numIslands(island)