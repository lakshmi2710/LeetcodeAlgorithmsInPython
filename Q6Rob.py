class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]

        mem = [-1] * len(nums)
        mem1 = [-1] * len(nums)

        return max(self.helper_rob(nums[:-1], len(nums) - 2, mem), self.helper_rob(nums[1:], len(nums) - 2, mem1))

    def helper_rob(self, nums, i, mem):
        if (len(nums) == 1):
            return nums[0]
        if (i < 0):
            return 0

        if mem[i] > 0:
            return mem[i]
        mem[i] = max(self.helper_rob(nums, i - 2, mem) + nums[i], self.helper_rob(nums, i - 1, mem))
        return mem[i]

