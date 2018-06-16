class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums: return [-1,-1]

        l = 0
        r = len(nums)-1

        while l<r:
            mid = (l+r)/2
            if nums[mid]< target:
                l = mid+1
            else:
                r = mid
        if nums[r] != target: return [-1,-1]

        left = r

        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l+r)/2
            if nums[mid]> target:
                r = mid
            else:
                l = mid +1
        if nums[r]!=target: r-=1

        right = r

        return [left,right]





test = Solution()
print test.searchRange([2,2],2)