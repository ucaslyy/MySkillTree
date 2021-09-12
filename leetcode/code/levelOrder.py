from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = [root]
        while len(stack):
            tmp_nodes = []
            tmp_vals = []
            for item in stack:
                if item:
                    tmp_nodes.append(item.left)
                    tmp_nodes.append(item.right)
                    tmp_vals.append(item.val)
            if tmp_vals:
                ans.append(tmp_vals)
            stack = tmp_nodes
        return ans
