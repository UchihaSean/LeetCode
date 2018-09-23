class Solution(object):
    def isPali(self, s):
        return s == s[::-1]

    def reverse(self, s):
        return s[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = set()
        dict = {}
        for i in range(len(words)):
            dict[words[i]] = i

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                if self.isPali(word[:j]):
                    s = self.reverse(word[j:])
                    if s in dict and dict[s] != i:
                        ans.add((dict[s], i))
                if self.isPali(word[j:]):
                    s = self.reverse(word[:j])
                    if s in dict and dict[s] != i:
                        ans.add((i, dict[s]))
        return map(list, ans)

