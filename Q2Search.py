class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        index = self.getIndex(nums, 0, len(nums) - 1)
        print index

        if index == -1:
            return self.binarySearch(nums, 0, len(nums) - 1, target)
        elif (nums[index] == target):
            return index
        elif (nums[0] > target):
            return self.binarySearch(nums, index + 1, len(nums) - 1, target)
        else:
            return self.binarySearch(nums, 0, index - 1, target)

    def getIndex(self, nums, low, high):
        print low, high
        if low > high or low == high:
            return -1

        mid = (low + high) / 2
        print mid, "mid"
        if nums[mid] < nums[mid - 1]:
            return mid - 1
        if nums[mid] > nums[mid + 1]:
            return mid

        if nums[mid] > nums[low]:
            return self.getIndex(nums, mid+1, high)
        else:
            return self.getIndex(nums, low, mid-1)

    def binarySearch(self, nums, low, high, target):
        if high < low:
            return -1

        mid = (low + high) / 2

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return self.binarySearch(nums, (mid + 1), high, target)
        else:
            return self.binarySearch(nums, low, (mid - 1), target);

nums = [3,4,5,6,1,2]
print nums
target = 2

sol = Solution()
print sol.search(nums, target)