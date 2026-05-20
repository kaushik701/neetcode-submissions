# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0: return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1,l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next 

        """
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
        """