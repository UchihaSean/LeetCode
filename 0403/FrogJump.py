class Solution(object):
    def bfs(self, stones):
        q = [[stones[0], 0]]
        marked = set()
        stones_set = set(stones)
        l = -1
        while l + 1 < len(q):
            l += 1
            i, k = q[l]
            # print(q)
            if i == stones[-1]: return True
            if i == stones[0]:
                if i + 1 in stones_set and (i + 1, 1) not in marked:
                    q.append([i + 1, 1])
                    marked.add((i + 1, 1))
            else:
                for j in range(k-1, k+2):
                    if j>0 and i+j in stones_set and (i+j, k) not in marked:
                        q.append([i+j, j])
                        marked.add((i+j, j))

        return False

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        return self.bfs(stones)


test = Solution()
print test.canCross([0, 1, 3, 5, 6, 8, 12, 17])
