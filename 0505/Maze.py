class Solution(object):
    def bfs(self, maze, start, f):
        f[start[0]][start[1]] = 0
        l = -1
        q = [[start[0], start[1], 0]]
        while l + 1 < len(q):
            l += 1
            x, y, dis = q[l]
            # print(x,y,dis)
            direct = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for x_p, y_p in direct:
                dis_p = 0
                x_n, y_n = x, y
                while 0 <= x_n + x_p < len(maze) and 0 <= y_n + y_p < len(maze[0]) and maze[x_n + x_p][y_n + y_p] == 0:
                    x_n += x_p
                    y_n += y_p
                    dis_p += 1
                if f[x_n][y_n] == -1 or f[x_n][y_n] > dis + dis_p:
                    f[x_n][y_n] = dis + dis_p
                    q.append([x_n, y_n, dis + dis_p])

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze: return -1
        f = [[-1 for j in range(len(maze[0]))] for i in range(len(maze))]
        self.bfs(maze, start, f)
        return f[destination[0]][destination[1]]
