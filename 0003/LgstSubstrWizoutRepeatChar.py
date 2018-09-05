class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict={}
        max_len = 0
        start = -1
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]]>start:
                    start = dict[s[i]]
                dict[s[i]] = i
            else:
                dict[s[i]]=i
            if max_len<i - start:
                    max_len = i-start

        return max_len


test = Solution()

print test.lengthOfLongestSubstring("pwwkew")