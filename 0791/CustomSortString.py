class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ans = ""
        dict = collections.defaultdict(int)
        for c in T:
            dict[c] += 1

        for c in S:
            if c in dict:
                ans += dict[c] * c
                dict[c] = 0

        for c in dict:
            ans += dict[c] * c
        return ans
