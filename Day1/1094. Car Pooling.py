trips = [[2,1,5],[3,3,7]]
capacity = 4
from heapq import *
def carpooling(trips, capacity):
    minHeap = []
    for i in range(len(trips)):
        heappush(minHeap, (trips[i][1], trips[i][0]))
        heappush(minHeap, (trips[i][2], -trips[i][0]))
    # print(minHeap)
    onBoarding = 0
    while minHeap:
        onBoarding += heappop(minHeap)[1]
        if onBoarding > capacity:
            return False
    return True

print(carpooling(trips, capacity))
    