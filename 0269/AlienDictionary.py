class Solution(object):
    def generate_pair(self, x, y):
        for i in range(min(len(x), len(y))):
            if x[i] != y[i]:
                if x[i] not in self.pair:
                    self.pair[x[i]] = [y[i]]
                else:
                    self.pair[x[i]].append(y[i])

                self.fin[y[i]] += 1
                break

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.pair = {}
        self.fin = {}
        for i in range(len(words)):
            for c in words[i]:
                self.fin[c] = 0
        for i in range(len(words) - 1):
            self.generate_pair(words[i], words[i + 1])

        ans = ""
        stack = []
        # print(self.fin)
        for x in self.fin:
            if self.fin[x] == 0:
                stack.append(x)
        # print(stack)
        while stack:
            x = stack.pop()
            ans += x
            if x not in self.pair: continue
            for y in self.pair[x]:
                # print(y, self.fin[y])
                self.fin[y] -= 1
                if self.fin[y] == 0:
                    stack.append(y)
        # print(self.fin)
        if len(ans)!=len(self.fin): return ""
        return ans


test = Solution()
print test.alienOrder(["ri"])
