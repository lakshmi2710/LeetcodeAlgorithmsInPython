class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minProduct = nums[0]
        maxProduct = nums[0]

        res = nums[0]

        for i in range(1, len(nums)):
            curMax = max(maxProduct * nums[i], nums[i], minProduct * nums[i])
            curMin = min(minProduct * nums[i], nums[i], maxProduct * nums[i])
            res = max(curMax, curMin, res)

            maxProduct = curMax
            minProduct = curMin
            curMax = curMax

        return res