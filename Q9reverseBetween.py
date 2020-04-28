# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dummy = prev = ListNode(0)
        prev.next = head

        cur = head
        count = 0
        while (count < m - 1):
            cur = cur.next
            prev = prev.next
            count = count + 1

        for i in range(n - m):
            front = cur.next
            cur.next = front.next
            front.next = prev.next
            prev.next = front

        return dummy.next