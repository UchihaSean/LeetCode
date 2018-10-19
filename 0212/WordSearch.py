class Trie:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.end = False


class Solution(object):
    def addWord(self, node, word):
        for c in word:
            if c not in node.child:
                node.child[c] = Trie(c)
            node = node.child[c]
        node.end = True

    def dfs(self, x, y, node, bo, now):
        if node.end:
            self.ans.add(now)

        dirt = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for x_p, y_p in dirt:

            if x + x_p < 0 or x + x_p >= len(bo) or y + y_p < 0 or y + y_p >= len(bo[0]): continue

            if not bo[x + x_p][y + y_p]: continue

            if bo[x + x_p][y + y_p] not in node.child: continue
            c = bo[x + x_p][y + y_p]
            bo[x + x_p][y + y_p] = None

            self.dfs(x + x_p, y + y_p, node.child[c], bo, now + c)
            bo[x + x_p][y + y_p] = c

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = Trie(0)
        for word in words:
            self.addWord(root, word)

        self.ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                bo = board[:][:]

                if bo[i][j] not in root.child: continue
                c = bo[i][j]
                bo[i][j] = None
                self.dfs(i, j, root.child[c], bo, c)
                bo[i][j] = c
        return list(self.ans)


board = [["a", "b"], ["a", "a"]]
words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]

test = Solution()
print test.findWords(board, words)
