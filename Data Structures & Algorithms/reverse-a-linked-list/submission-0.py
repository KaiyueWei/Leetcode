# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        nextNode = head.next
        head.next = None
        while nextNode:
            old = head
            head = nextNode
            nextNode = nextNode.next
            head.next = old
        return head
        


        