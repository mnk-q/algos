def insertionSort2(n, arr):
    for i in range(n-1):
        j, key = i, i+1
        while(arr[j]>arr[key] and j>=0):
            arr[j],arr[key] = arr[key],arr[j]
            j-=1
            key-=1
        print(*arr)