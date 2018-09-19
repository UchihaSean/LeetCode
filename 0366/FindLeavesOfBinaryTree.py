# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, leaves):
        if not node.left and not node.right:
            leaves[0].append(node.val)
            return 0
        left = right = -1
        if node.left:
            left = self.dfs(node.left, leaves)
        if node.right:
            right = self.dfs(node.right, leaves)
        leaves[max(left, right) + 1].append(node.val)
        return max(left, right) + 1

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        leaves = [[] for _ in range(50)]
        n = self.dfs(root, leaves)
        return leaves[:n + 1]
