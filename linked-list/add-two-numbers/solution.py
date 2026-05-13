from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        a, b = l1, l2
        while a or b or carry:
            x = a.val if a else 0
            y = b.val if b else 0
            total = x + y + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            if a:
                a = a.next
            if b:
                b = b.next
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
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print(to_list(sol.addTwoNumbers(l1, l2)))
    print(to_list(sol.addTwoNumbers(build_list([0]), build_list([0]))))
