
def partition(arr, low, high):
    pi = high
    swap = low

    for i in range(low, high):
        if arr[i] < arr[pi]:
            arr[swap], arr[i] = arr[i], arr[swap]
            swap += 1

    arr[swap], arr[pi] = arr[pi], arr[swap]
    return swap


def quickSort(arr, low, high):
    if low >= high:
        return
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)
    return arr


arr = [3,10,2,5,8,11,6,4]
print quickSort(arr, 0, len(arr)-1)