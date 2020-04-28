class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = list()
        hash = {}

        for num in nums2:

            while len(stack) > 0 and stack[-1] < num:
                hash[stack.pop()] = num
            stack.append(num)

        while len(stack) > 0:
            hash[stack.pop()] = -1

        res = list()
        for nums in nums1:
            res.append(hash[nums])
        return res
