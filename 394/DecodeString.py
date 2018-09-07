class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                if len(stack) != 0 and stack[-1].isdigit():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
                continue
            if s[i] == '[':
                stack.append('[')
                continue
            if s[i].isalpha():
                if len(stack) != 0 and stack[-1].isalpha():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
                continue
            if s[i] == ']':
                alpha = ""
                while stack[-1].isalpha():
                    alpha = stack.pop()+alpha
                stack.pop()
                number = stack.pop()
                # print(number)
                # print(alpha)
                stack.append(int(number) * alpha)
                # print(stack)

        return "".join(stack)


test = Solution()
print test.decodeString("3[a2[c]]")
