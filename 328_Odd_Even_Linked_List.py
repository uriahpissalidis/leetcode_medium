class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or  head.next is None):
            return head
        # assign odd = head(starting node of ODD)
        # assign even = head.next(starting node of EVEN)
        odd  , even  =  head , head.next
        
        Even = even # keep starting point of Even Node so later we will connect with Odd Node
        while(odd.next and even.next):
            odd.next = odd.next.next # Connect odd.next to odd Node
            even.next = even.next.next # Connect even,next to Even Node
            
            odd = odd.next # move odd 
            even = even.next # move even
        
        odd.next = Even # now connect odd.next to starting point to Even list
        
        return head
