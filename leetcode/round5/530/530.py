# 530. Minimum Absolute Difference in BST
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        md = inf
        prev = None
        def solve(n):
            nonlocal md, prev
            if n == None:
                return
            solve(n.left)
            if prev is not None:
                md = min(md, n.val - prev.val)

            prev = n
            solve(n.right)
        solve(root)
        return md