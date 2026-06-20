from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return int(best)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxPathSum(root))
    print(sol.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
    print(sol.maxPathSum(TreeNode(-3)))
