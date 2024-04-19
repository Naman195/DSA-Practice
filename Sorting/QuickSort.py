def QuickSort(arr, lb, ub):
    if(lb < ub):
        pos = Partition(arr, lb, ub)
        QuickSort(arr, lb, pos-1)
        QuickSort(arr, pos+1, ub)

def Partition(arr, lb, ub):
    pivot = arr[lb]
    cnt = 0
    for i in range(lb+1, ub+1):
        if arr[i] <= pivot:
            cnt += 1
    
    pivotIndex = cnt + lb
    
    arr[lb], arr[pivotIndex] = arr[pivotIndex], arr[lb]
    
    start = lb
    end = ub
    
    while(start < pivotIndex and end > pivotIndex):
        while(arr[start] <= pivot):
            start += 1
        while(arr[end] > pivot):
            end -= 1
        
        if(start < pivotIndex and end > pivotIndex):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return pivotIndex


arr = [21,1,2,52,13,96,54,10]
n = len(arr)
print(arr)          

print(QuickSort(arr, 0, n-1))  

print(arr)          
        