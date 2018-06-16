class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def turn_order(dx, dy):
            """
            turn the direction
            """
            "East to South"
            if dy == 1: return 1, 0
            "South to West"
            if dx == 1: return 0, -1
            "West to North"
            if dy == -1: return -1, 0
            "North to East"
            if dx == -1: return 0, 1

            return dx, dy

        "Special Case"
        if matrix == []: return []

        "Initial State"
        x, y = 0, 0
        dx, dy = 0, 1
        "Final answer"
        spiral_order = []
        isVisited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]

        "Cycle to get the spiral order"

        while True:
            "Add the num to spiral order"
            # print x, y
            isVisited[x][y] = True
            spiral_order.append(matrix[x][y])
            "All num visited"
            if len(spiral_order) == len(matrix) * len(matrix[0]): break
            "next position"
            next_x, next_y = x+dx, y+dy
            "check whether to turn"
            if next_x == -1 or next_x == len(matrix) or next_y == -1 or next_y == len(matrix[0])\
                    or isVisited[next_x][next_y]:
                dx, dy = turn_order(dx, dy)

            x, y = x+dx, y+dy


        return spiral_order







matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

test = Solution()
print test.spiralOrder(matrix)