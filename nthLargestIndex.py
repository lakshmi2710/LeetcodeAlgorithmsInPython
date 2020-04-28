def maxIndex(arr):
    """
    :param arr:
    :return:
    """
    max = arr[0]
    if len(arr) < 1:
        return -1

    for i in range(len(arr)):
        if arr[i]>=max:
            max = arr[i]
            index = i
        else:
            continue
    return index

if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    value = maxIndex(arr)
    print value