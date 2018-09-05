class Solution(object):
    def generate(self, rowIndex):

        line = [0 for i in range(rowIndex+1)]

        for i in range(rowIndex+1):
            line[i] = 1
            for j in range(i - 1, 0, -1):
                line[j] += line[j - 1]
        return line


test = Solution()
print test.generate(0)
