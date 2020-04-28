class Solution(object):
    def removeZeroSumSublists(self, head):
        prefixSum = 0
        hashmap = {}
        dummy = ListNode(0)

        dummy.next = head

        while (head):
            prefixSum = prefixSum + head.val
            hashmap[prefixSum] = head
            head = head.next

        head = dummy
        prefixSum = 0

        while (head):
            prefixSum = prefixSum + head.val
            if prefixSum in hashmap.keys():
                head.next = hashmap[prefixSum].next
            head = head.next
        return dummy.next