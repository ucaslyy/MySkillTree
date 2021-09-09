# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = None  # 反转后的首节点
        while head is not None:
            pre = curr
            curr = head
            head = head.next
            curr.next = pre
        return curr
