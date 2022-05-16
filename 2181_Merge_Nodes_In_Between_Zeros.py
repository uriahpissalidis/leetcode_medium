class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointers and variables
        ptr1 = head
        ptr2 = head.next
        s = 0
        
        while ptr2:
            #if ptr2's value doesn't equal 0, add the value to the sum
            if ptr2.val != 0:
                s += ptr2.val
            else:
                #assuming we hit another 0, move set the pointer to the next one
                #and set the sum to 0
                ptr1 = ptr1.next
                ptr1.val = s
                s = 0
            ptr2 = ptr2.next
            
        ptr1.next=None
        return head.next