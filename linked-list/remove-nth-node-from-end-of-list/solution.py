from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next:
            slow.next = slow.next.next

        return dummy.next


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
    print(to_list(sol.removeNthFromEnd(head1, 2)))
    head2 = build_list([1])
    print(to_list(sol.removeNthFromEnd(head2, 1)))
    head3 = build_list([1, 2])
    print(to_list(sol.removeNthFromEnd(head3, 1)))
