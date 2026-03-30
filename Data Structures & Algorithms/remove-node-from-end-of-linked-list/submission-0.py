# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, head: Optional[ListNode], n: int) -> int:
        if head.next == None:
            return 0
        count = 1 + self.helper(head.next, n)
        if count == n:
            head.next = head.next.next
        return count
             
            

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        self.helper(dummy, n)
        return dummy.next

        