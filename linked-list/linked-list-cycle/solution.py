from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def build_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    sol = Solution()
    head1 = build_cycle([3, 2, 0, -4], 1)
    print(sol.hasCycle(head1))
    head2 = build_cycle([1, 2], 0)
    print(sol.hasCycle(head2))
    head3 = build_cycle([1], -1)
    print(sol.hasCycle(head3))
