def fibonacci_search(arr,n,target):
    offset=-1
    f2=0
    f1=1
    f=f2+f1
    while f<n:
        f2=f1
        f1=f
        f=f2+f1
    while f>1:
        i=min(offset+f2,n-1)
        if arr[i]<target:
            f=f1
            f1=f2
            f2=f-f1
            offset=i
        elif arr[i]>target:
            f=f2
            f1=f1-f2
            f2=f-f1
        else:
            return 1
    if f1==1 and arr[offset+1]==target:
        return offset +1
    return -1