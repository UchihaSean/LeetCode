class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dfs(res, nums, 0)
        return res


def swap(nums, i, j):
    s = nums[i]
    nums[i] = nums[j]
    nums[j] = s


def dfs(res, nums, k):
    # print(nums, k)
    if k == len(nums)-1:
        res.append(nums[:])
        return
    for i in range(k, len(nums)):
        swap(nums, k, i)
        dfs(res, nums, k + 1)
        swap(nums, k, i)


test = Solution()
print(test.permute([1, 2, 3, 4]))
