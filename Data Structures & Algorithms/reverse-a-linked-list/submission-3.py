# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head == None:
            return None
        # base case, head.next is None, this is the tail of the original list
        if head.next == None:
            newhead = head
            return newhead
        
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead



        