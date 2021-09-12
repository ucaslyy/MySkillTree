# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代方法
    def isSymmetric(self, root: TreeNode) -> bool:
        left_stack = [root]
        right_stack = [root]
        while left_stack and right_stack:
            left_root = left_stack.pop()
            right_root = right_stack.pop()
            if not left_root and not right_root:
                continue
            elif not left_root or not right_root:
                return False
            else:
                if left_root.val == right_root.val:
                    left_stack.append(left_root.left)
                    left_stack.append(left_root.right)
                    right_stack.append(right_root.right)
                    right_stack.append(right_root.left)
                else:
                    return False
        return not left_stack and not right_stack

    # 递归方法
    # def isSymmetric(self, root: TreeNode) -> bool:
    #
    #     def dfs(left_tree, right_tree):
    #         if not left_tree and not right_tree:
    #             return True
    #         elif not left_tree or not right_tree:
    #             return False
    #
    #         if left_tree.val == right_tree.val:
    #             if not dfs(left_tree.left, right_tree.right):
    #                 return False
    #             if not dfs(left_tree.right, right_tree.left):
    #                 return False
    #         else:
    #             return False
    #         return True
    #
    #     if root is None:
    #         return True
    #     else:
    #         return dfs(root.left, root.right)
