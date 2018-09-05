class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        f = [[-9999999 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        s = [[-9999999 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]


        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                if i==0 and j==0:
                    f[i][j] = s[i][j] = dungeon[i][j]

