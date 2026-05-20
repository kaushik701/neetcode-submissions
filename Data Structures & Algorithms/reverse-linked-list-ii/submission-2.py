# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        dummy.next = head
        # 1) reach node at position "left"
        left_prev, curr = dummy, head
        for _ in range(left-1):
            left_prev, curr = curr, curr.next
        
        # now cur="left", leftprev="node before left"
        # 2) reverse from left to right
        prev = None
        for _ in range(right-left+1):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 3) update pointers
        left_prev.next.next = curr # curr is node after "right"
        left_prev.next = prev # prev is "right"
        return dummy.next