# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        stack = [root]
        while len(stack):
            tmp_nodes = []
            flag = False
            for item in stack:
                if item:
                    tmp_nodes.append(item.left)
                    tmp_nodes.append(item.right)
                    flag = True
            if flag:
                max_depth += 1
            stack = tmp_nodes
        return max_depth
