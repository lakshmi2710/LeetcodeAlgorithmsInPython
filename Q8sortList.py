# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        return self.mergeSort(head)

    def mergeSort(self, head):

        if (head == None or head.next == None):
            return head

        mid = self.getMidNode(head)
        newHead = mid.next
        mid.next = None

        return self.merge(self.mergeSort(head), self.mergeSort(newHead))

    def getMidNode(self, head):
        slow = head
        fast = head

        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        head = ListNode(None)
        temp = head

        a = list1
        b = list2

        while (a != None and b != None):
            if (a.val < b.val):
                temp.next = a
                a = a.next
                temp = temp.next
            else:
                temp.next = b
                b = b.next
                temp = temp.next
        while (a != None):
            temp.next = a
            a = a.next
            temp = temp.next

        while (b != None):
            temp.next = b
            b = b.next
            temp = temp.next

        return head.next