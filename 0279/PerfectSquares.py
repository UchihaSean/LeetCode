import numpy as np
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [-1 for _ in range(n+1)]
        f[0] = 0
        for i in range(n+1):
            if f[i] == -1: continue
            for j in range(int(np.sqrt(n-i))+1):
                if i+j*j<=n and (f[i+j*j]==-1 or f[i+j*j]>f[i]+1):
                    f[i+j*j] = f[i]+1
        return f[n]