class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = [1]+nums[:]+[1]
        f = [[-1 for j in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)-1):
            f[i][i+1] = 0
        for k in range(2, len(nums)):
            for i in range(len(nums) - k):
                for j in range(i+1, i+k):
                    if f[i][i+k]==-1 or f[i][i+k]<f[i][j] + f[j][i+k] + nums[i]*nums[j]*nums[i+k]:
                        f[i][i+k] = f[i][j] + f[j][i+k] + nums[i]*nums[j]*nums[i+k]
        # print(f)
        return f[0][len(nums)-1]