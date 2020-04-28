class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if(n == 0):
            return
        prodArray = [1]*n
        prod = 1
        for i in range(1,n):
            prod = prod * nums[i-1]
            prodArray[i] = prod
        prod = 1
        for i in range(n-2,-1,-1):
            prod = prod * nums[i+1]
            prodArray[i] = prod * prodArray[i]
        return prodArray