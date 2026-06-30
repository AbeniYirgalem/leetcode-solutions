from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result: List[str] = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if idx < len(values):
                if values[idx] != "#":
                    node.left = TreeNode(int(values[idx]))
                    queue.append(node.left)
                idx += 1
            if idx < len(values):
                if values[idx] != "#":
                    node.right = TreeNode(int(values[idx]))
                    queue.append(node.right)
                idx += 1
        return root


def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result: List[Optional[int]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = codec.serialize(root)
    new_root = codec.deserialize(data)
    print(to_list(new_root))
    print(codec.serialize(None))
    print(to_list(codec.deserialize(codec.serialize(TreeNode(1)))))
