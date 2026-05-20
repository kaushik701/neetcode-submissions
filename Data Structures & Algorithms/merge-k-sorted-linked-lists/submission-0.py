# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

         # Allow ListNode comparison by value for heap
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
        
        # Initialize heap with non-null heads
        min_heap = [node for node in lists if node]
        heapify(min_heap)

        # dummy head to build result
        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            node = heappop(min_heap)
            tail.next = node
            tail = tail.next

            if node.next: heappush(min_heap, node.next)
        return dummy.next