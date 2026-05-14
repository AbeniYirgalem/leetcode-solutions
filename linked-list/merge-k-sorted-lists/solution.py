import heapq
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap: List[Tuple[int, int, ListNode]] = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        tail = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
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
    lists1 = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    print(to_list(sol.mergeKLists(lists1)))
    print(to_list(sol.mergeKLists([])))
