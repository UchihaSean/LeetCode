class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        file_system = input.split("\n")
        directory = []
        max_length = 0
        length = []
        print(file_system)

        for i in range(len(file_system)):
            # print(length)
            level = calculate_level(file_system[i])
            # print(level)
            if level < len(directory):
                directory = directory[:level]
                length = length[:level]
            directory.append(file_system[i])
            if len(length) == 0:
                length.append(len(file_system[i]) - level + 1)
            else:
                length.append(length[-1] + len(file_system[i]) - level+ 1)
            if is_file(file_system[i]):
                if length[-1] - 1 > max_length:
                    max_length = length[-1] - 1
        return max_length


def calculate_level(s):
    return s.count("\t")


def is_file(s):
    for i in range(len(s) - 1):
        if s[i] == '.':
            return True
    return False


test = Solution()
print test.lengthLongestPath(
    "dir\n        file.txt")
# print calculate_level('\tts')
# print(is_file('\tab'))