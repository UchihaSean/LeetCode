import heapq
class Solution(object):
    def addskyline(self, x, y):
        if y!= self.skyline[-1][1]:
            self.skyline.append([x,y])
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        pointX = set([s[0] for s in buildings]+[s[1] for s in buildings])

        buildings_heap = []
        i = 0
        self. skyline = [[-1, 0]]

        for x in sorted(pointX):
            while i<len(buildings) and buildings[i][0]<=x:
                heapq.heappush(buildings_heap, (-buildings[i][2], buildings[i][1]))
                i+=1

            while buildings_heap and buildings_heap[0][1]<=x:
                heapq.heappop(buildings_heap)



            height = -buildings_heap[0][0] if buildings_heap else 0
            self.addskyline(x, height)

        return self.skyline[1:]




test = Solution()
print(test.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ] ))