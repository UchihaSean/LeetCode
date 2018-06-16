class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for str in sorted(strs):
            key = tuple(sorted(str))
            if key in group:
                group[key]+=[str]
            else:
                group[key] = [str]

        return group.values()





test = Solution()
print test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])