from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
    print(sol.isValidBST(root1))
    print(sol.isValidBST(root2))
