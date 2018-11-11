class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        a_s = set()
        for c in s:
            if c in a_s:
                dic[c] -= 1
                continue
            while len(stack) > 0 and c < stack[-1] and dic[stack[-1]] > 1:
                dic[stack[-1]] -= 1
                a_s.remove(stack[-1])
                stack.pop()
            stack.append(c)
            a_s.add(c)

        print(stack)
        ans = ""
        a_s = set()
        for c in stack:
            if c in a_s: continue
            ans += c
            a_s.add(c)
        return ans
