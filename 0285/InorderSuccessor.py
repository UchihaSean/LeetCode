# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        if node.left: self.dfs(node.left)
        if self.p == None:
            self.successor = node
            self.p = node
            return None
        if node == self.p: self.p = None

        if node.right: self.dfs(node.right)

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        self.successor = None
        self.p = p
        self.dfs(root)
        return self.successor
