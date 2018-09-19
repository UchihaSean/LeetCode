# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, target, ans):
        if node.left:
            self.dfs(node.left, target, ans)
        if node.val <= target:
            self.index = len(ans)
        ans.append(node.val)
        if node.right:
            self.dfs(node.right, target, ans)

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root: return root
        ans = []
        self.index = 0
        self.dfs(root, target, ans)

        left = max(0, self.index - k / 2)
        right = left + k - 1
        while left > 0 and abs(ans[left - 1] - target) < abs(ans[right] - target):
            left -= 1
            right -= 1
        while right < len(ans) - 1 and abs(ans[left] - target) > abs(ans[right + 1] - target):
            right += 1
            left += 1
        return ans[left:right + 1]