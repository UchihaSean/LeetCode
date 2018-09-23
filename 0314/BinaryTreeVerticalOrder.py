# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bfs(self, root, res):
        q = [[root, 0]]
        l = -1
        while l + 1 < len(q):
            l += 1
            node, depth = q[l]
            if not node: continue
            if depth > self.max:
                self.max = depth
            if depth < self.min:
                self.min = depth
            if depth in res:
                res[depth].append(node.val)
            else:
                res[depth] = [node.val]
            if node.left:
                q.append([node.left, depth - 1])
            if node.right:
                q.append([node.right, depth + 1])

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = {}
        self.max = -99999
        self.min = 99999
        self.bfs(root, res)
        # print(res)
        ans = []
        for i in range(self.min, self.max + 1):
            if i in res:
                ans.append(res[i])

        return ans
