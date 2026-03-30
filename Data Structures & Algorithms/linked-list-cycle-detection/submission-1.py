# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        iterator = head
        seen = set()
        while iterator:
            if iterator in seen:
                return True
            seen.add(iterator)
            iterator = iterator.next
        return False

        