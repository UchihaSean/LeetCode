class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = []

        for num in nums:
            if ans ==[] or ans[-1]==num:
                ans.append(num)
            else:
                ans.pop()

        return ans[-1]

test = Solution()
print test.majorityElement([2,1,2,1,1])
