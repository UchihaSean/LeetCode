# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        if not node: return 0
        if not node.left and not node.right: return 1
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.max_length = max(self.max_length, left, right)
        if node.left and node.val + 1 == node.left.val:
            left += 1
        else:
            left = 0
        if node.right and node.val + 1 == node.right.val:
            right += 1
        else:
            right = 0
        self.max_length = max(self.max_length, left, right)
        return max(left, right, 1)

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.max_length = 1
        self.dfs(root)
        return self.max_length


