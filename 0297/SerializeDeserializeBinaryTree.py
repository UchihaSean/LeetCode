# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        stack = [root]
        data = [root.val]
        index = 0
        while index < len(stack):
            node = stack[index]
            index += 1

            # left
            if node.left:
                stack.append(node.left)
                data.append(node.left.val)
            else:
                data.append(None)

            # right
            if node.right:
                stack.aappend(node.right)
                data.append(node.right.val)
            else:
                data.append(None)

        # print(data)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        head = root = TreeNode(data[0])
        index = 0
        l = 0
        stack = [root]
        while l < len(stack):
            node = stack[l]
            # print(node.val)
            l += 1
            index += 1
            if index < len(data) and data[index] is not None:
                node.left = TreeNode(data[index])
                stack.append(node.left)
            index += 1
            if index < len(data) and data[index] is not None:
                node.right = TreeNode(data[index])
                stack.append(node.right)

        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))