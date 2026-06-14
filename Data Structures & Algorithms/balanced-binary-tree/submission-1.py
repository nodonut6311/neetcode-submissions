class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )

    def isBalanced(self, root):
        if not root:
            return True

        hl = self.maxDepth(root.left)
        hr = self.maxDepth(root.right)

        return (
            abs(hl - hr) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )