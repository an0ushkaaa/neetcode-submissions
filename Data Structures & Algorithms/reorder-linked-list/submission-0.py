# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow.next
        slow.next=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        left=head

        while prev:
            left_next=left.next
            prev_next=prev.next
            left.next=prev
            prev.next=left_next
            left=left_next
            prev=prev_next
            
        

