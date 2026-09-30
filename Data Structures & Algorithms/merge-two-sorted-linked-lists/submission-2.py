# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        curr = list1
        prev = list2

        while curr and prev:
            if curr.val < prev.val:
                node.next = curr
                curr = curr.next
            else:
                node.next = prev
                prev = prev.next
            node = node.next

        node.next = curr or prev
        return dummy.next  # ← Return from dummy, not node!
