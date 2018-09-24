class Solution(object):
    def next_int(self, s, i):
        res = 0
        while i < len(s) and s[i] not in '+-()':
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        return (res, i)

    def dfs(self, s):
        stack = []
        i = 0
        mul = 1
        mul_lis = []
        while i < len(s):
            if s[i] == '(':
                if len(mul_lis) == 0:
                    mul_lis.append(mul)
                else:
                    mul_lis.append(mul_lis[-1] * mul)
                i += 1
                continue
            if s[i] == ')':
                # print(mul_lis)
                mul_lis.pop()
                i+=1
                continue
            if s[i] in '0123456789':
                mul = 1
                if i>0 and s[i-1]=='+':
                    mul = 1
                if i>0 and s[i-1]=='-':
                    mul = -1
                res, i = self.next_int(s, i)

                if len(mul_lis) > 0:
                    stack.append(mul_lis[-1]*mul * res)
                else:
                    stack.append(mul * res)
                continue
            if s[i] == '+':
                mul = 1
                i += 1
                continue

            if s[i] == '-':
                mul = -1
                i += 1
                continue
        return sum(stack)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        return self.dfs(s)
test = Solution()
print test.calculate("1-(5)")