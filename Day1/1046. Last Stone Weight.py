from heapq import *
stones = [2,7,4,1,8,1]

def lastStone(arr):
    maxHeap = []
    for i in arr:
        heappush(maxHeap, -i)
    
    while len(maxHeap) > 1:
        x = -heappop(maxHeap)
        y = -heappop(maxHeap)
        if x!= y:
            heappush(maxHeap, -(x-y))
    if(len(maxHeap) == 1):
        return -heappop(maxHeap)
    else:
        return 0
    
print(lastStone(stones))