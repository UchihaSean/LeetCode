class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        j=0
        min_len=100000000
        for i in range(len(strs)):
            if len(strs[i])<min_len:
                min_len=len(strs[i])
        common=""
        while True:
            if j == min_len: return common
            common= strs[0][:j+1]
            for i in range(len(strs)):
                if common!=strs[i][:j+1]: return common[:-1]
            j+=1
        return 0


test = Solution()
print test.longestCommonPrefix([""])