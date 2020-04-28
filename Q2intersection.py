""" // Question: 2

    /*
     * Given two arrays, write a function to compute their intersection. Example 1:
     * Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2] Note: Each element in the
     * result must be unique. The result can be in any order.
     */

    public Integer[] intersection(Integer[] nums1, Integer[] nums2) {
        throw new Exception("Not Implemented");
"""

def intersection(nums1, nums2):
    """

    :param nums1:
    :param nums2:
    :return:
    """

    hash = {}
    res = []

    for i in nums1:
        hash[i] = True

    for j in set(nums2):
        if j in hash:
            res.append(j)

    return res

nums1 = (1,2,2,1,3)
nums2 = (2,2,3)

print intersection(nums1,nums2)






