# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not next: return head
        prev = head
        curr = head.next

        while curr:
            g = gcd(prev.val,curr.val)
            new_node = ListNode(g,curr)
            prev.next = new_node

            prev = curr
            curr = curr.next
        return head