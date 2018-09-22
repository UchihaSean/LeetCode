class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPali(s[l:r]) or isPali(s[l + 1:r + 1])
            l += 1
            r -= 1
        return True


def isPali(s):
    return s == s[::-1]


test = Solution()
print(test.validPalindrome("abca"))
