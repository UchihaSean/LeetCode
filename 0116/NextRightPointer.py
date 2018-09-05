# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if root == None: return None
        nodeList = []
        l = -1
        r = 0
        nodeList.append([root, 0])

        while l < r:
            l += 1
            if nodeList[l][0].left!=None:
                r+=1
                nodeList.append([nodeList[l][0].left,nodeList[l][1]+1])
            if nodeList[l][0].right!=None:
                r+=1
                nodeList.append([nodeList[l][0].right, nodeList[l][1] + 1])

        for i in range(len(nodeList)-1):
            if nodeList[i][1]==nodeList[i+1][1]:
                nodeList[i][0].next = nodeList[i+1][0]
