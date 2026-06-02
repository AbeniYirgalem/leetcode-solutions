from typing import Optional, Dict, List


class Node:
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None) -> None:
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        clones: Dict[Node, Node] = {}
        current = head
        while current:
            clones[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            clones[current].next = clones.get(current.next)
            clones[current].random = clones.get(current.random)
            current = current.next

        return clones[head]


def build_random_list(values: List[int], random_indices: List[Optional[int]]) -> Optional[Node]:
    if not values:
        return None
    nodes = [Node(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, rand_idx in enumerate(random_indices):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]


def serialize(head: Optional[Node]) -> List[List[Optional[int]]]:
    if not head:
        return []
    nodes: List[Node] = []
    index_map: Dict[Node, int] = {}
    current = head
    while current:
        index_map[current] = len(nodes)
        nodes.append(current)
        current = current.next
    result: List[List[Optional[int]]] = []
    for node in nodes:
        rand_idx = index_map.get(node.random)
        result.append([node.val, rand_idx])
    return result


if __name__ == "__main__":
    sol = Solution()
    head1 = build_random_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copy1 = sol.copyRandomList(head1)
    print(serialize(copy1))
    head2 = build_random_list([1, 2], [1, 1])
    copy2 = sol.copyRandomList(head2)
    print(serialize(copy2))
    head3 = build_random_list([], [])
    copy3 = sol.copyRandomList(head3)
    print(serialize(copy3))
