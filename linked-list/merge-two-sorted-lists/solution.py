from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        a, b = list1, list2
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next

if __name__ == "__main__":
    def build_list(values):
        dummy = ListNode(0)
        tail = dummy
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    sol = Solution()
    head1 = build_list([1, 2, 4])
    head2 = build_list([1, 3, 4])
    print(to_list(sol.mergeTwoLists(head1, head2)))
    print(to_list(sol.mergeTwoLists(build_list([]), build_list([0]))))
