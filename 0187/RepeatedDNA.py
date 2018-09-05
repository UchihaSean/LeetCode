class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) < 10: return []

        str = s[:10]
        dict = {}

        dict[str] = 1

        for i in range(10, len(s)):
            str = str[1:] + s[i]

            if str not in dict:
                dict[str] = 1
            else:
                dict[str] += 1

        return [key for key in dict if dict[key] > 1]


test = Solution()
print test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")