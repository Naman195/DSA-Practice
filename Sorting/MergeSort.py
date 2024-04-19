def mergeSort(arr, low, high):
    if(low >= high):
        return
    mid = (low + high) //2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    return arr


def merge(arr, low, mid, high):
    left = low
    right = mid+1
    
    res = []
    
    while left <= mid and right <= high:
        if(arr[left] <= arr[right]):
            res.append(arr[left])
            left += 1
        else:
            res.append(arr[right])
            right += 1
    
    while left <= mid:
        res.append(arr[left])
        left += 1
    while right <= high:
        res.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = res[i-low]
        
        
        
        
arr = [21,1,2,52,13,96,54,10]

n = len(arr)

print(mergeSort(arr, 0, n-1))

# print(arr)
        