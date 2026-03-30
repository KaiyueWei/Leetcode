# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## find the middle of the linked list
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slow points to the end of the first segment
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        #prev points to the head of the second reversed segment
        first = head
        second = prev
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        return None






        
        