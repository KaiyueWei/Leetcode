# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #slow points to the end of the first segment
        prev = None
        cur = slow.next
        slow.next = None
        nex = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        # prev pointing to the head of the second reversed list
        # two list: first , head: head, tail: slow
        #           second, head: prev, tail: second
        first = head
        while prev:
            tmp1, tmp2 = first.next, prev.next
            first.next = prev
            prev.next = tmp1
            first, prev = tmp1, tmp2
        return None





        
        