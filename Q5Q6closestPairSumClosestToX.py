"""  // Question: 5
    // Find closest pair from two sorted arrays
    /*
     * There are two sorted arrays, and a number X. Find two numbers one from each
     * array such that sum of both of them comes closest to number X
     *
     * Input: arr1[] = {5, 6, 8, 10, 24}; arr2[] = {12, 15, 20, 25, 30}; x = 51
     * Output: 24 and 25
     *
     *
     */
    // Question: 6
    public void closestPairSumClosestToX(Integer[] arr1, Integer[] arr2) {
        throw new Exception("Not Implemented");
    }"""


def closestPairSumClosestToX2(arr1,arr2,x):
    l = 0
    h = len(arr2)-1
    diff = abs(x-(arr1[l]+arr2[h]))

    while(l<len(arr1) and h>=0):
        total = (arr1[l] + arr2[h])
        if abs(x-total) < diff:
            diff = abs(x-total)
            num1 = arr1[l]
            num2 = arr2[h]

        if total > x:
            h = h-1
        else:
            l = l+1
    return num1, num2

arr1 = [5, 6, 8, 10, 24]
arr2 = [12, 15, 20, 25, 30]
x = 51

print closestPairSumClosestToX2(arr1,arr2,x)


