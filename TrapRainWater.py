class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water_height =[]
        cover =0
        for i in range(len(height)):
            if height[i]>cover:
                cover = height[i]
            water_height.append(cover)
        cover = 0
        for i in range(len(height)-1,-1,-1):

            if height[i]>cover:
                cover = height[i]
            if cover<water_height[i]:
                water_height[i]=cover

        water_sum = 0
        for i in range(len(water_height)):
            water_sum+=water_height[i] - height[i]
        return water_sum


test = Solution()
print test.trap([0,2,0])