"""// Question: 10
    /*
     * Check if there are duplicates in k distance
     *
     * There is a string and we have to figure out if there are duplicates in K
     * distance. Input: string: "ABCADEB", K = 3 Output : false
     *
     * Input: string: "ABACDEB", K = 3 Output : true
     *
     */
    public Integer duplicatesInKDistance(Integer[] arr, Integer k) {
        throw new Exception("Not Implemented");
    }
}
"""


def duplicatesInKDistance(arr, K):
    hash = {}
    i =0
    while i < len(arr):

        if i>K-1:

            hash[arr[i-K]]=False

        if(hash.get(arr[i],False)):
            return True
        else:
            hash[arr[i]]=True
            i = i + 1


    return False


arr = "ABACDEB"
K=3
print "result = %s"%duplicatesInKDistance(arr,K)