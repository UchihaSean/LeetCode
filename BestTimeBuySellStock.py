class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if prices == []: return 0
        k = min(k, len(prices)/2+1)
        f = [[0 for i in range(k + 1)] for j in range(len(prices))]
        g = [-prices[i] for i in range(len(prices))]
        for i in range(1, len(prices)):
            g[i] = max(g[i-1], g[i])

        for t in range(1, k + 1):
            for i in range(1, len(prices)):
                f[i][t] = max(f[i - 1][t], g[i-1]+prices[i])

            for i in range(1, len(prices)):
                g[i] = max(g[i-1], f[i][t] - prices[i])

        return max(f[len(prices) - 1])


test = Solution()
print test.maxProfit(2, [6, 1, 3, 2, 4, 7])
