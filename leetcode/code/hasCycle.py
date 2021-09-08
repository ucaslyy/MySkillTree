# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        解法一：快慢指针，每一次，快指针走2步，慢指针走1步
        :param head:
        :return:
        """
        if head is None:
            return False
        pNode = head  # 快指针
        qNode = head  # 慢指针
        while pNode is not None:
            if pNode.next is not None:
                pNode = pNode.next.next
            else:
                return False
            if qNode is not None:
                qNode = qNode.next

            if qNode == pNode:
                return True

        return False
