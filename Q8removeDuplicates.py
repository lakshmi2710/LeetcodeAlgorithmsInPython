"""// Question: 8
    /*
     * Remove Duplicates from Sorted Array Given a sorted array nums, remove the
     * duplicates in-place such that each element appear only once and return the
     * new length. Do not allocate extra space for another array, you must do this
     * by modifying the input array in-place with O(1) extra memory.
     *
     * Example 1: Given nums = [1,1,2], Your function should return length = 2, with
     * the first two elements of nums being 1 and 2 respectively. Example 2: Given
     * nums = [0,0,1,1,1,2,2,3,3,4], Your function should return length = 5, with
     * the first five elements of nums being modified to 0, 1, 2, 3, and 4
     * respectively.
     */
    public Integer removeDuplicates(Integer[] arr) {
        throw new Exception("Not Implemented");
    }"""


def removeDuplicates(arr):
    if len(arr)==0:
        return 0
    count =1
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            arr[count] = arr[i]
            count = count + 1
    return count



arr = [0,0,1,1,1,2,2,3,3,4]

print removeDuplicates(arr)
