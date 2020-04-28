""" // Question: 3

    /*
     * Let's call an array A a mountain if the following properties hold: A.length
     * >= 3 There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ...
     * A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] Given an array that is
     * definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i]
     * > A[i+1] > ... > A[A.length - 1].
     *
     * Example 1: Input: [0,1,0] Output: 1 Example 2: Input: [0,2,1,0] Output: 1
     */
    public Integer peakIndexInMountainArray(Integer[] A) {
        throw"""


def peakIndexInMountainArray(arr):
    """
    :type A: List[int]
    :rtype: int
    """
    index = 0

    for i in range(len(arr)):
        if arr[i] > arr[i + 1]:
            return i
    return -1

arr = [0,2,1,0]

print peakIndexInMountainArray(arr)