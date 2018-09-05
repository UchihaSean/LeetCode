class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        if not nums: return -1
        pivot = -1
        l = 0
        r = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                pivot = i
                if target>nums[pivot] or target<nums[pivot+1]: return -1
                if nums[0]<=target:
                    l = 0
                    r = pivot
                else:
                    l = pivot+1
                    r = len(nums)-1
                break
        # print l,pivot,r
        if pivot==-1:
            l = 0
            r =len(nums)-1
        while l<r:
            mid = (l+r)/2
            if nums[mid]<target:
                l = mid +1
            else:
                r = mid
        if nums[r] == target: return r

        return -1



test = Solution()
print test.search([1,3],3)