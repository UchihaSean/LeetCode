class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l + 1 < r:
            mid = (l + r) / 2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid - 1] > nums[mid]:
                r = mid - 1
                continue

            if nums[mid + 1] > nums[mid]:
                l = mid + 1
                continue

        if nums[r]>nums[l]: l=r
        return l


test = Solution()
print test.findPeakElement([1,2,1,3,5,6,4])
