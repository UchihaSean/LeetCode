class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len=0
        center=0
        for i in range(len(s)):
            lenth=1
            j=1
            while i-j>-1 and i+j<len(s) and s[i-j]==s[i+j]:
                lenth+=2
                j+=1
            if lenth>max_len:
                max_len=lenth
                center=i

            if i+1<len(s) and s[i]==s[i+1]:
                lenth=2
                j=1
                while i-j>-1 and i+1+j<len(s) and s[i-j]==s[i+1+j]:
                    lenth+=2
                    j+=1
                if lenth>max_len:
                    max_len=lenth
                    center=i

        return s[center-(max_len-1)/2:center+max_len/2+1]




test=Solution()
print test.longestPalindrome("babad")