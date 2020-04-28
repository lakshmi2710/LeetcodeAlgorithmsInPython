class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None or head.next.next == None:
            return head

        ptr1 = head
        ptr2 = ptr1.next
        evenhead = ptr2

        while (ptr1.next and ptr1.next.next):
            ptr1.next = ptr2.next
            ptr2.next = ptr1.next.next
            ptr1 = ptr1.next
            if (ptr2.next != None):
                ptr2 = ptr2.next

        ptr2.next = None
        ptr1.next = evenhead

        return head