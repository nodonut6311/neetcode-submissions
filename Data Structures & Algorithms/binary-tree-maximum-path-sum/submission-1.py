# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSum(self, node):
        if not node:
            return 0

        ls = max(0, self.maxSum(node.left))
        rs = max(0, self.maxSum(node.right))

        self.res = max(self.res, ls + rs + node.val)
        return max(ls, rs) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        self.maxSum(root)
        return self.res