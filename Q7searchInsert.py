class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0] or target == nums[0]:
            return 0

        return self.bs(nums, target, 1, len(nums) - 1)

    def bs(self, nums, target, low, high):
        if (low > high):
            return
        mid = (low + high) / 2
        if nums[mid] == target or nums[mid - 1] < target < nums[mid]:
            return mid
        elif nums[mid] > target:
            return self.bs(nums, target, 0, mid - 1)
        else:
            return self.bs(nums, target, mid + 1, high)




