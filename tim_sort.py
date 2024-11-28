def tim_sort(arr):
    min_run=32
    n=len(arr)
    for i in range(0,n,min_run):
          insertion_sort(arr,i,min(i+min_run-1,(n-1)))
    size=min_run
    while size<n:
        for start in range(0,n,size*2):