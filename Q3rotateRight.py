# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        ptr1 = ptr2 = head
        count = self.getCount(head)
        if k >= count:
            k = k % count
            print k

        while (k > 0 and ptr1.next):
            ptr1 = ptr1.next
            k = k - 1
        while (ptr1.next):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = head
        head = ptr2.next
        ptr2.next = None

        return head

    def getCount(self, head):
        temp = head
        count = 0
        while (temp):
            temp = temp.next
            count = count + 1
        return count
