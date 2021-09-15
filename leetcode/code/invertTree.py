# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)

        return root
