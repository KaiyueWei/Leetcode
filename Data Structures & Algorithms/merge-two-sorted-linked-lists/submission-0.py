# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        iterator1 = list1
        iterator2 = list2

        dumb = ListNode()
        if iterator1.val < iterator2.val:
            head = iterator1
            iterator1 = iterator1.next
        else:
            head = iterator2
            iterator2 = iterator2.next
        
        dumb = head

        while iterator1 and iterator2:
            if iterator1.val <= iterator2.val:
                dumb.next = iterator1
                iterator1 = iterator1.next
            else:
                dumb.next = iterator2
                iterator2 = iterator2.next
            dumb = dumb.next
        
        if iterator1:
            dumb.next = iterator1
        if iterator2:
            dumb.next = iterator2
        
        return head
        