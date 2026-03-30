# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initialize the pointers
        prev = None
        cur = head
        nex = None

        #iterate the list
        while cur != None:
            # save the cur's next
            nex = cur.next
            # reverse the pointer
            cur.next = prev
            # update the pointers
            prev = cur
            cur = nex
        return prev
        


        