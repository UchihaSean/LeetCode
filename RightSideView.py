# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def dfs(self, node, deep):
        if len(self.rightView) == deep:
            self.rightView.append(node.val)
        if node.right:
            self.dfs(node.right, deep + 1)
        if node.left:
            self.dfs(node.left, deep + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.rightView = []
        self.dfs(root, 0)
        return self.rightView
