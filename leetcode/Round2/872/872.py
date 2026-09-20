# 872. Leaf-Similar Trees
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = self.solve(root1)
        seq2 = self.solve(root2)
        return  seq1 == seq2
    def solve(self, root) -> list:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()

            if not node.left and not node.right:
                res.append(node.val)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res