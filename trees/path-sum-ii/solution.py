from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []

        def dfs(node: Optional[TreeNode], remaining: int, path: List[int]) -> None:
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                result.append(path[:])
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)
            path.pop()

        dfs(root, targetSum, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5,
                    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    print(sol.pathSum(root, 22))
    print(sol.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 3))
    print(sol.pathSum(None, 0))
