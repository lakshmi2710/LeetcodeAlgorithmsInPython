def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        y = target - nums[i]
        if dict.get(y, False):
            return [i, dict[y]]
        else:
            dict[nums[i]] = i

nums = [1,2,3,4,5]
target = 4
print twoSum(nums, target)