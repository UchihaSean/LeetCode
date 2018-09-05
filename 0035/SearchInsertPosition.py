class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        nums.append(target+1)
        l = 0
        r = len(nums) -1
        while l<r:
            mid = (l+r)/2
            if nums[mid]< target:
                l = mid+1
            else:
                r = mid
        return r



test = Solution()
print test.searchInsert([1,3,5,6],7)