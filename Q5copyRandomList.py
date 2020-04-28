"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        copyMap = {}
        cur = head

        # make full copy
        copyMap[None] = None
        while cur != None:
            copyMap[cur] = Node(cur.val, None, None)
            cur = cur.next

        # make new list
        newHead = copyMap[head]
        cur = head
        newCur = newHead
        while cur != None:
            newCur.next = copyMap[cur.next]
            newCur.random = copyMap[cur.random]
            cur = cur.next
            newCur = newCur.next

        return newHead