def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i- 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [21,1,2,52,13,96,54,10]
print(bubbleSort(arr))