class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)-k
        self.quickSort(nums, 0, len(nums) - 1, n)
        return nums[k * -1]

    def partition(self, nums, low, high):
        pi = high
        swap = low

        for i in range(low, high):
            if nums[i] < nums[pi]:
                nums[swap], nums[i] = nums[i], nums[swap]
                swap += 1

        nums[swap], nums[pi] = nums[pi], nums[swap]
        return swap

    def quickSort(self, nums, low, high,n):
        if low >= high:
            return
        pi = self.partition(nums, low, high)
        if n > pi:
            self.quickSort(nums, pi + 1, high, n)
        else:
            self.quickSort(nums, low, pi-1, n)