class Solution(object):
    def bfs(self, x, y, rooms):
        l = -1
        q = [[x, y, 0]]
        while l + 1 < len(q):
            l += 1
            x, y, dis = q[l]
            if x > 0 and rooms[x - 1][y] > dis + 1:
                rooms[x - 1][y] = dis + 1
                q.append([x - 1, y, dis + 1])
            if x < len(rooms) - 1 and rooms[x + 1][y] > dis + 1:
                rooms[x + 1][y] = dis + 1
                q.append([x + 1, y, dis + 1])
            if y > 0 and rooms[x][y - 1] > dis + 1:
                rooms[x][y - 1] = dis + 1
                q.append([x, y - 1, dis + 1])
            if y < len(rooms[0]) - 1 and rooms[x][y + 1] > dis + 1:
                rooms[x][y + 1] = dis + 1
                q.append([x, y + 1, dis + 1])

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(i, j, rooms)
