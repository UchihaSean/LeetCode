# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_path_sum = -9999999
        self.dfs(root)

        return self.max_path_sum

    def dfs(self,node):

        left_sum = 0
        right_sum = 0
        if node.left is not None:
            left_sum = max(0,self.dfs(node.left))
        if node.right is not None:
            right_sum = max(0,self.dfs(node.right))

        if self.max_path_sum< node.val+left_sum+right_sum:
            self.max_path_sum = node.val+left_sum+right_sum

        return node.val+max(left_sum,right_sum)



root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

test = Solution()
print test.maxPathSum(root)