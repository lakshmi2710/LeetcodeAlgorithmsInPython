# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head

        dummy = ListNode(None)

        prev = dummy
        prev.next = head

        start = head
        end = head.next

        head = prev

        while (start != None and end != None):

            if (start.val == end.val):
                while (end != None and start.val == end.val):
                    end = end.next
                prev.next = end
                start = end
                if end != None:
                    end = end.next
            else:
                prev = start
                start = start.next
                end = end.next
        head = dummy.next
        return head
