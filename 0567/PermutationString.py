class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        dict1 = {}
        for i in range(26):
            dict1[chr(i + ord('a'))] = 0
        for c in s1:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        dict2 = {}
        for i in range(26):
            dict2[chr(i + ord('a'))] = 0
        for i in range(len(s1)):
            if s2[i] in dict2:
                dict2[s2[i]] += 1
            else:
                dict2[s2[i]] = 1
        if dict2 == dict1: return True
        for j in range(len(s1), len(s2)):
            dict2[s2[j - len(s1)]] -= 1
            if s2[j] in dict2:
                dict2[s2[j]] += 1
            else:
                dict2[s2[j]] = 1
            if dict2 == dict1: return True
        return False
