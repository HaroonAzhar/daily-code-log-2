# 104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return root
        return self.solve(root,1)
    def solve(self,root:Optional[TreeNode], depth:int) -> int:
        left, right = 0 ,0
        left = self.solve(root.left, depth + 1) if root.left else depth
        right = self.solve(root.right, depth + 1) if root.right else depth
        return max(left, right)