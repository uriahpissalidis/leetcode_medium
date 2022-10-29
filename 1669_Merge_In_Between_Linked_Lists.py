class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
            # 1. Find last node which will be left after deletion
            # 2. Find first node from the second part which will be left
            # 3. Insert list2 between them

            start = end = list1
            for idx in range(0, a - 1):
                start, end = start.next, end.next
            for idx in range(0, b - a + 2):
                end = end.next

            start.next = list2
            while list2 and list2.next:
                list2 = list2.next
            list2.next = end

            return list1