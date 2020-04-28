# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if (head == None or head.next == None):
            head

        fast = slow = head

        while (fast != None):
            fast = fast.next
            if (fast != None):
                fast = fast.next
                slow = slow.next

        return slow

