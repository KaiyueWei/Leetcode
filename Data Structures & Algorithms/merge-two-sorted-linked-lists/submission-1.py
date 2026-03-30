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

        dummy = ListNode()
        node = dummy

        while iterator1 and iterator2:
            if iterator1.val <= iterator2.val:
                node.next = iterator1
                iterator1 = iterator1.next
            else:
                node.next = iterator2
                iterator2 = iterator2.next
            node = node.next
        
        if iterator1:
            node.next = iterator1
        if iterator2:
            node.next = iterator2
        
        return dummy.next
        