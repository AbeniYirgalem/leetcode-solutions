from typing import List, Optional, Dict


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map: Dict[int, int] = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = index_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(root.val)
    print(sol.buildTree([1], [1]).val)
    print(sol.buildTree([], []))
