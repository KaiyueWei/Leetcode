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

        while iterator:
            if iterator.val == 'seen':
                return True
            iterator.val = 'seen'
            iterator = iterator.next
        return False

        