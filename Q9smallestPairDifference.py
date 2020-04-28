"""
  // Question: 9
    /*
     * Smallest Difference pair between two sorted arrays
     *
     * There are two sorted arrays, we have to find the pair which has smallest
     * difference,
     */
    public Integer smallestPairDifference(Integer[] arr) {
        throw new Exception("Not Implemented");
    }

"""

def smallestPairDifference(A, B):
    a =0
    b = 0
    num1 = A[0]
    num2 = B[0]
    diff = abs(A[0]-B[0])
    while a < (len(A)) and b < (len(B)):
        if abs(A[a]-B[b])<diff:
            diff = abs(A[a]-B[b])
            num1 = A[a]
            num2 = B[b]
        if(A[a]>B[b]):
            b = b+1
        else:
            a = a+1
    return num1,num2

A = [10, 11, 12]
B = [1, 2]
print smallestPairDifference(A,B)
