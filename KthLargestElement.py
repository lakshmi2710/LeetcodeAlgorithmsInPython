def partition(arr, low, high):
    pi = high
    swap = low

    for i in range(low, high):
        if arr[i] < arr[pi]:
            arr[swap], arr[i] = arr[i], arr[swap]
            swap += 1

    arr[swap], arr[pi] = arr[pi], arr[swap]
    return swap

def quickSort(arr, low, high, n):
    if low >= high:
        return
    pi = partition(arr, low, high)
    if n > pi:
        quickSort(arr, pi + 1, high, n)
    else:
        quickSort(arr, low, pi-1, n)

def findKthLargest(arr, k):
    n = len(arr)-k
    quickSort(arr,0,len(arr)-1, n)
    return arr[k*-1]

arr = [3,2,3,1,2,4,5,5,6]
# print quickSort(arr, 0, len(arr)-1)
print findKthLargest(arr, k = 4)