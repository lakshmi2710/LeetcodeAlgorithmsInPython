# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1 = l1.val
        num2 = l2.val

        l1 = l1.next
        l2 = l2.next

        while (l1 != None):
            num1 = (num1 * 10) + l1.val
            l1 = l1.next

        while (l2 != None):
            num2 = (num2 * 10) + l2.val
            l2 = l2.next
        print num1, num2

        res = num1 + num2

        if res == 0:
            return ListNode(0)

        prev = head = None
        while (res > 0):
            item = res % 10
            res = res / 10
            print item

            node = ListNode(item)
            if prev is None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

        return head

