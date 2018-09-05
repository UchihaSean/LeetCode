class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(5, n + 1,5):
            t = i
            while True:
                if t % 5 != 0: break
                t = t / 5
                ans += 1

        return ans

test = Solution()
print test.trailingZeroes(10000000)