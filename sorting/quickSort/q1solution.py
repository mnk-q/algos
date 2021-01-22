def quickSort(arr,start,end):
    if(start<end):
        pivot = arr[end]
        i = start-1
        if(start<end):
            for j in range(start,end):
                if(arr[j]<pivot):
                    i=i+1
                    arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[end] = arr[end],arr[i+1]
        mid = i+1
        quickSort(arr, start, mid-1) 
        quickSort(arr, mid+1, end) 
    return arr


def findit(ms, ns, m, n):
    ms = quickSort(ms,0,m-1)
    ns = quickSort(ns,0,n-1)
    j=0
    if(m>n):
        return 'NO'
    for i in range(m):
        while(j<n):
            if(ms[i]>ns[j]):
                j=j+1
                break
            else:
                j+=1
        if(j==n):
            return 'NO'
    return 'YES'


# Write your code here
tc = int(input())
ans = []
for t in range(tc):
    mn = input().split()
    m =  int(mn[0])
    n = int(mn[1])
    ms = list(map(int, input().split()))
    ns = list(map(int, input().split()))
    try:
        ans.append(findit(ms,ns,m,n))
    except:
        print(e)
for i in ans:
    print(i)