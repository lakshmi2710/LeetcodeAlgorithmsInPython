class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(len(dp)):
            for j in range(len(nums)):
                print i, nums[j], "i,nums[j]"
                if (i - nums[j] >= 0):
                    dp[i] = dp[i] + dp[i - nums[j]]

        return dp[target]
