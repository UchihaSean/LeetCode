# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result = 0
        pre = root
        while root:
            if not root.left:
                k -= 1
                if k == 0:
                    result = root.val
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if pre.right:
                    k -= 1
                    if k == 0:
                        result = root.val
                    root = root.right
                    pre.right = None
                else:
                    pre.right = root
                    root = root.left

        return result
