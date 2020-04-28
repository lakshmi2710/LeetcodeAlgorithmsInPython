# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        extra = ListNode(-1)
        extra.next = head

        cur = extra
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next

            cur.next = sec
            first.next = sec.next

            sec.next = first
            cur = cur.next.next

        head = extra.next
        return head