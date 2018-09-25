class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        error = 0
        if len(s) > len(t):
            s, t = t, s
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    error += 1
            if error != 1: return False
            return True
        elif len(t) - len(s) == 1:
            for i in range(len(t)):
                if t[:i] + t[i + 1:] == s:
                    return True
            return False
        else:
            return False
