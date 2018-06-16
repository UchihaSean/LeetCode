class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # Split path and delete . and None
        directs = [p for p in path.split('/') if p!='' and p!='.']

        # Test
        # print directs

        # store path
        stack = []

        # cycle directs
        for direct in directs:
            # no back
            if direct!='..':
                stack.append(direct)
            elif stack!=[]:
                stack.pop()

        return '/'+'/'.join(stack)




test = Solution()
print test.simplifyPath("/..")