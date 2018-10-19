class Solution(object):
    def merge_sort(self, s, l, r):
        if l == r:
            return [s[l]]
        mid = (l + r) / 2
        sl = self.merge_sort(s, l, mid)
        sr = self.merge_sort(s, mid + 1, r)
        sa = []
        ldx = 0
        rdx = 0
        while ldx < len(sl) and rdx < len(sr):
            if sl[ldx][0] <= sr[rdx][0]:
                sl[ldx][1] += rdx
                sa.append(sl[ldx])
                ldx += 1
            else:
                sa.append(sr[rdx])
                rdx += 1
        while ldx < len(sl):
            sl[ldx][1] += rdx
            sa.append(sl[ldx])
            ldx += 1
        while rdx < len(sr):
            sa.append(sr[rdx])
            rdx += 1
        # print(sa)
        return sa

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        s = []
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            s.append([nums[i], 0, i])
        s = self.merge_sort(s, 0, len(s) - 1)
        for i in range(len(s)):
            ans[s[i][2]] = s[i][1]
        return ans

