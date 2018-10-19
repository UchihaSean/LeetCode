class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = [-1 for _ in range(amount + 1)]
        f[0] = 0
        for i in range(amount + 1):
            if f[i] == -1: continue
            for coin in coins:
                if i + coin <= amount and (f[i + coin] == -1 or f[i + coin] > f[i] + 1):
                    f[i + coin] = f[i] + 1
        # print(f)
        return f[amount]

