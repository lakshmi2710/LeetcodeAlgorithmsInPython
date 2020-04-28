import sys
"""
// Question: 7
    // K Closest numbers to a number X
    /*
     * There is a sorted array, and a number X. We want to find K closest elements
     * to a number X
     *
     * Input: arr1[] = {5, 6, 8, 10,12,21, 24,25,32,37,45,51 }; k = 4 X = 23 Output:
     * [24,25,21]
     */

    public Integer[] kClosestToX(Integer[] arr, Integer k, Integer x) {
        throw new Exception("Not Implemented");
    }
"""

def kClosestToX(arr, k, x):

    diff = sys.maxsize

    for i in range(len(arr)):
        if(abs(arr[i]-x)<diff):
            diff = abs(arr[i]-x)
            nearest = arr[i]
            index = i
    print nearest
    left = index-k
    right = index+k
    if k == 1:
        return [nearest]

    if left <0:
        left = 0
    if right > len(arr)-1:
        right = len(arr)-1

    while(abs(left-right) > k-1):

        if(abs(arr[left]-x)>abs(arr[right]-x)):
            left = left +1
        else:
            right = right -1
    return arr[left:right+1]
arr = [5, 6, 8, 10,12,21, 24,25,32,37,45,51]
k = 4
x = 23
print kClosestToX(arr, k, x)