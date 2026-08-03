# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        mpp = {}
        q = deque([(root,0)])

        while q:
            node, row = q.popleft()
            mpp[row] = node.val

            if node.left:
                q.append((node.left, row + 1))
            if node.right:
                q.append((node.right, row + 1))
        
        return [mpp[key] for key in sorted(mpp)]