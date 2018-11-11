class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = []
        for num in nums:
            if len(ans) > 2: break
            if not ans:
                ans.append(num)
                continue
            if num > ans[-1]:
                ans.append(num)
            else:
                for i in range(len(ans)):
                    if ans[i] >= num:
                        ans[i] = num
                        break

        # print(ans)
        return len(ans) == 3
