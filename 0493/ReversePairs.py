class Solution(object):
    def merge_sort(self, nums, i, j):
        if i == j:
            return nums[i:j + 1]
        mid = (i + j) / 2
        left = self.merge_sort(nums, i, mid)
        right = self.merge_sort(nums, mid + 1, j)
        merge = []
        l_i, r_i = 0, 0
        while l_i < len(left) and r_i < len(right):
            if left[l_i] <= 2 * right[r_i]:
                l_i += 1
            else:
                self.sum += len(left) - l_i
                r_i += 1

        l_i, r_i = 0, 0
        while l_i < len(left) and r_i < len(right):
            if left[l_i] < right[r_i]:
                merge.append(left[l_i])
                l_i += 1
            else:
                merge.append(right[r_i])
                r_i += 1
        if l_i < len(left): merge.extend(left[l_i:])
        if r_i < len(right): merge.extend(right[r_i:])
        return merge

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        self.sum = 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.sum