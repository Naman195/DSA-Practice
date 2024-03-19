from heapq import *
x = [1,4,5,3,7,8,6,10]
k = 3
def kthLargest(arr, k):
    minHeap = []
    for i in range(len(arr)):
        heappush(minHeap, arr[i])
        # print(minHeap)
        
        if(len(minHeap) == k+1):
            heappop(minHeap)
    # print(minHeap)
    # ans = []
    ans = []
    for i in range(k):
        ans.append(heappop(minHeap))
    print(ans[0])
    
kthLargest(x, k)
    
    