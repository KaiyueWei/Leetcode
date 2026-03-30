# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: head is None
        if head == None:
            return None
        # store the old next node
        nextNode = head.next
        # set the head to be the tail
        head.next = None
        # iterate through the list
        while nextNode:
            # store the old head
            old = head
            # set nextNode to be the new head
            # head and nextNode are pointing to the same node
            head = nextNode
            # update nextNode first
            nextNode = nextNode.next
            # update the node
            head.next = old
        return head
        


        