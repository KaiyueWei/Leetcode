# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1, list2) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        
        dummy = ListNode()
        dummy.next = None

        iterator = dummy

        while node1 and node2:
            if node1.val < node2.val:
                iterator.next = node1
                node1 = node1.next
            else:
                iterator.next = node2
                node2 = node2.next
            iterator = iterator.next
        if node1:
            iterator.next = node1
        if node2:
            iterator.next = node2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        new_list = lists[0]
        for i in range(1,n):
            new_list = self.merge(new_list, lists[i])
        return new_list
        