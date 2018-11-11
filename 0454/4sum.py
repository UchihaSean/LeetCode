class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i] + B[j] not in dic:
                    dic[A[i] + B[j]] = 1
                else:
                    dic[A[i] + B[j]] += 1
        ans = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if -C[i] - D[j] in dic:
                    ans += dic[-C[i] - D[j]]
        return ans
