def fibonacci_search(arr,n,target):
    offset=-1
    f2=0
    f1=1
    f=f2+f1
    while f<n:
        f2=f1
        f1=f
        f=f2+f1
