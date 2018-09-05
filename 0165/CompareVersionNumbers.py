class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(len(v1) - len(v2)):
            v2.append(0)
        for i in range(len(v2) - len(v1)):
            v1.append(0)

        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v2[i]) > int(v1[i]):
                return -1

        return 0


test = Solution()
print test.compareVersion("01","1")
