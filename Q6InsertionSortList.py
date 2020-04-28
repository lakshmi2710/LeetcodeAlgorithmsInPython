# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if head is None: return head

        dummy = ListNode(None)
        dummy.next = head
        cur = head

        while (cur.next != None):

            if (cur.val < cur.next.val):
                print "1st IF", cur.val, cur.next.val
                cur = cur.next
            else:
                target = cur.next
                print "target", target.val
                if cur.next.next is not None:
                    cur.next = cur.next.next
                else:
                    cur.next = None

                loopcur = dummy
                while (loopcur.next != None):
                    if loopcur.next.val < target.val:
                        loopcur = loopcur.next
                    else:
                        print "loop", loopcur.next.val
                        target.next = loopcur.next
                        loopcur.next = target
                        break
        return dummy.next
