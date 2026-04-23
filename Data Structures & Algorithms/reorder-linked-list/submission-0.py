# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of the linked list

        fast=slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        # reverse second half of list
        second=slow.next
        prev=slow.next=None

        while second:
            next=second.next
            second.next=prev
            prev=second
            second=next
        
        first=head
        second=prev

        while second:
            h1=first.next
            h2=second.next

            first.next=second
            second.next=h1
            first, second = h1, h2


        


        