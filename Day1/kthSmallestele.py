from heapq import *
x = [1,4,5,3,7,8,6,10]
k = 3

def kthSamllest(arr, k):
    maxHeap = []
    for i in range(len(arr)):
        heappush(maxHeap, -arr[i])
    
        if(len(maxHeap) == k+1):
            heappop(maxHeap)
    print(maxHeap)

kthSamllest(x, k)
    