# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head

        start = head
        end = head.next

        while (start != None and end != None):

            if (start.val == end.val):
                while (end != None and start.val == end.val):
                    end = end.next
                start.next = end
                start = end
                if end != None:
                    end = end.next
            else:
                start = start.next
                end = end.next
        return head
