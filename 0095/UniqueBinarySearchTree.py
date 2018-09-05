# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(nums):
            if len(nums)==0: return [None]


            node_list = []
            for i in range(len(nums)):

                left_node = dfs(nums[:i])
                right_node = dfs(nums[i+1:])

                # print node.val,[t.val for t in left_node if t!=None],[t.val for t in right_node if t!=None]

                for left in left_node:
                    for right in right_node:
                        node = TreeNode(nums[i])
                        node.left = left
                        node.right = right
                        node_list.append(node)

            return node_list



        sol = dfs(range(1,n+1))
        return sol


test = Solution()
test.generateTrees(3)