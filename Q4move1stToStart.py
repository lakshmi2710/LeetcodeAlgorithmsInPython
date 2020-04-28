""" // Question: 4
    // Move all 1's to start of an array in a Binary array.
    /*
     * Binary array is an array with numbers 0 and 1, we have to move all the 1's to
     * start of the array in O(n) without extra memory. Do not use count sort. Count
     * sort will do the job in 2*O(n), Hint think like dutch flag
     *
     * e.g. Input: [1,0,1,0,0,0,1,0,1,1,0] Output: [1,1,1,1,1,0,0,0,0,0,0]
     *
     *
     */

    public void move1sToStart(Integer[] arr) {
        throw new Exception("Not Implemented");
    }
"""

def move1sToStart(arr):
    start = 0
    end = len(arr)-1
    pivot = 0

    while(pivot < end):
        if arr[pivot]==0:
            arr[end], arr[pivot] = arr[pivot], arr[end]
            end = end - 1

        if arr[pivot]==1:
            start = start + 1
            pivot = pivot + 1

    return arr


arr=[1,0,0,0,0,1,1,1,1,0,1,0,1]
print move1sToStart(arr)

print arr