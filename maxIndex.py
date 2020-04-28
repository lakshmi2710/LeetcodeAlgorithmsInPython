class Solution(object):
    def maxIndex(self, arr):
        """
        :param arr:
        :return:
        """
        max = arr[0]
        index = 0

        if len(arr) < 1:
            return -1

        for i in range(len(arr)):
            if arr[i]>max:
                max = arr[i]
                index = i

        return index