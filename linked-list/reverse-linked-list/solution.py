from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    sol = Solution()
    head1 = build_list([1, 2, 3, 4, 5])
    print(to_list(sol.reverseList(head1)))
    head2 = build_list([1])
    print(to_list(sol.reverseList(head2)))
    head3 = build_list([])
    print(to_list(sol.reverseList(head3)))
