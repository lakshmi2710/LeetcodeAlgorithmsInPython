"""
 // Question: 1
    /*
     * Given an array of integers, return indices of the two numbers such that they
     * add up to a specific target. You may assume that each input would have
     * exactly one solution, and you may not use the same element twice.
     *
     * Example: Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] =
     * 2 + 7 = 9, return [0, 1].
     */

    public Integer[] twoSum(Integer[] nums, Integer target) {

        throw new Exception("Not Implemented");
    }
"""

def twoSum(nums, target):
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



nums=(2, 7, 11, 15)
target = 9

print twoSum(nums,target)