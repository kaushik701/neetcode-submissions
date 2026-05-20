# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: break

            groupNext = kth.next # node after the kth group

            prev, curr = groupNext, groupPrev.next

            # Reverse the group between groupPrev.next and kth
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # Reconnect reversed group with previous part and move groupPrev
            tmp = groupPrev.next # tmp = old head of the group (now tail)
            groupPrev.next = kth # new head of group
            groupPrev = tmp # move groupPrev to tail for next round
        return dummy.next
