# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        p_head = p_temp = ListNode(-1, head)
        while p_temp.next is not None:
            if p_temp.next.val == val:
                p_temp.next = p_temp.next.next
            else:
                p_temp = p_temp.next

        return p_head.next
