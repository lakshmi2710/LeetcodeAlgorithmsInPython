class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hash:
                return [hash[y], i]
            else:
                hash[nums[i]] = i

        return [-1, -1]
