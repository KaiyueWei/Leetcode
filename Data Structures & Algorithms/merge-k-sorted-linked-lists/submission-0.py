# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        first = lists[0]
        second = lists[1]
        print(f'first:{first}')
        print(f'second:{second}')
        dummy = ListNode()
        prev = dummy
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            if first.val >= second.val:
                prev.next = second
                prev = second 
                second = tmp2
            else:
                prev.next = first
                prev = first
                first = tmp1
        if first:
            prev.next = first
        if second:
            prev.next = second
        # new merged list: dummy.next
        rest = lists[2:]
        return self.mergeKLists([dummy.next] + rest)

        