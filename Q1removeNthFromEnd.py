class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        ptr1 = ptr2 = head
        count = 0
        prev = None

        while (count < n and ptr1):
            ptr1 = ptr1.next
            count = count + 1

        if (count < n):
            print "length of linked list is smaller than n value"
            return

        while (ptr1):
            prev = ptr2
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if prev == None:
            head = head.next
            return head

        prev.next = ptr2.next
        return head
