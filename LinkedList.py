class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def printlist(self, head):
        print "List data are"
        res = []
        temp = self.head
        while(temp):
            res.append(temp.data)
            temp = temp.next
        print res

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node




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

            while (res > 0):
                item = res % 10
                res = res / 10
                print item

                node = Node(item)
                node.next = self.head
                self.head = node
            return self.head




