def insertionSort(a):
    ar = []
    arr = a.copy()
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
           arr[j+1] = arr[j]
           j -= 1
        arr[j+1] = key
    for i in a:
        ar.append(arr.index(i)+1)
    return ar