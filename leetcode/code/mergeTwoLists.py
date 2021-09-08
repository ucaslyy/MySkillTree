# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = ph = ListNode(-1)
        pl1 = l1
        pl2 = l2
        while pl1 is not None and pl2 is not None:
            if pl1.val > pl2.val:
                ph.next = pl2
                pl2 = pl2.next
            else:
                ph.next = pl1
                pl1 = pl1.next
            ph = ph.next

        if pl1 is not None:
            ph.next = pl1

        if pl2 is not None:
            ph.next = pl2

        return head.next
