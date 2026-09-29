# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initiate prev and curr
    #iterate while curr is not empty
    #inititate our after to reatin the rest of the list
    #flip our curr to point to our prev
    # shift both prev and curr by one
        prev = None
        curr = head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev