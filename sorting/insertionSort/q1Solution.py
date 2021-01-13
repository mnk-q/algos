def insertionSort1(n, arr):
    for i in range(len(arr)-1):
        st,key = i,i+1
        if(arr[st]>arr[key]):
            while(arr[st]>arr[key] and st>=0):
                t = arr[key]
                arr[key]=arr[st]
                print(*arr)
                arr[st] = t
                st-=1
                key-=1
    print(*arr)