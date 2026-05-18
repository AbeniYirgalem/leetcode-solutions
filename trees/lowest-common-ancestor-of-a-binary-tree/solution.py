from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left
    q = root.right
    print(sol.lowestCommonAncestor(root, p, q).val)
    p = root.left
    q = root.left.right.right
    print(sol.lowestCommonAncestor(root, p, q).val)
