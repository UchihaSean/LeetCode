# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True
        if node.left and node.right:
            left = self.dfs(node.left)
            right = self.dfs(node.right)
            if left and right and node.left.val == node.right.val == node.val:
                self.count += 1
                return True
            return False
        if node.left:
            left = self.dfs(node.left)
            if left and node.left.val == node.val:
                self.count += 1
                return True
            return False
        if node.right:
            right = self.dfs(node.right)
            if right and node.right.val == node.val:
                self.count += 1
                return True
            return False

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.count = 0
        self.dfs(root)
        return self.count
