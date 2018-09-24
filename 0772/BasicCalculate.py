class Solution(object):
    def next_int(self, s, i):
        res = 0
        if s[i] == '(':
            j = i + 1
            left = 1
            while j < len(s):
                if s[j] == '(': left += 1
                if s[j] == ')': left -= 1
                if left == 0:
                    break
                j += 1
            res = self.dfs(s[i + 1:j])
            i = j + 1
            return res, i
        while i < len(s) and s[i] not in '+-*/()':
            res = res * 10 + ord(s[i]) - ord('0')
            i += 1
        return res, i

    def dfs(self, s):
        stack = []
        tmp, i = self.next_int(s, 0)
        if i != 0:
            stack.append(tmp)
        while i < len(s):
            op = s[i]
            tmp, i = self.next_int(s, i + 1)
            if op == '+':
                stack.append(tmp)
            elif op == '-':
                stack.append(-tmp)
            elif op== '*':
                stack[-1]*=tmp
            else:
                if stack[-1]>=0:
                    stack[-1]/=tmp
                else:
                    stack[-1] = - ((-stack[-1])/tmp)

        return sum(stack)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        return self.dfs(s)
test = Solution()
test.calculate("")
