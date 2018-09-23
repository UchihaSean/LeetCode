class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        self.helper(num, 0, target, 0, 0, "", results)
        return results

    def helper(self, string, start, target, sum_so_far, last, path, results):
        if start == len(string) and sum_so_far == target:
            results.append(path)

        for end in range(start + 1, len(string) + 1):
            sub_string = string[start:end]
            if len(sub_string) > 1 and sub_string[0] == '0':
                break
            cur = int(sub_string)
            if start == 0:
                self.helper(string, end, target, sum_so_far + cur, cur, path + sub_string, results)
            else:
                self.helper(string, end, target, sum_so_far + cur, cur, path + "+" + sub_string, results)
                self.helper(string, end, target, sum_so_far - cur, -cur, path + "-" + sub_string, results)
                self.helper(string, end, target, sum_so_far - last + cur * last, cur * last, path + "*" + sub_string,
                            results)