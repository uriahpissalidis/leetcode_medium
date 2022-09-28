class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) runtime (One Pass Solution)
        # O(1) memory complexity
        fast = slow = head
        for _ in range(n): 
            fast = fast.next # skip n nodes
        # If fast == None at the end of the loop that means that the end is actually the first node.
        if fast == None: 
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # change the pointer before to the pointer after the target node
        return head
        
        
        # O(2n) == O(n) runtime
        # O(1) memory complexity
        if head.next == None:
            return None
        
        # find length of the linked lists
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        # index to delete is length - n
        index = length - n 
        if index == 0:
            return head.next
        
        # remove that node 
        # link the prev node to the next node 
        curr = head
        i = 1
        while curr:
            if i == index:
                curr.next = curr.next.next
                break
            curr = curr.next
            i += 1
        
        return head