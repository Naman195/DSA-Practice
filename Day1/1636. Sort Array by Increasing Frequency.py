from heapq import *
nums = [1,1,2,2,2,3]
# nums = [2,3,1,3,2]


def sortfreq(arr):
    mp = {}
    for i in arr:
        mp[i] = mp.get(i, 0) + 1
    # print(mp)
    maxHeap = []
    for key, val in mp.items():
        heappush(maxHeap, (val, key))
    print(maxHeap)
    ans = []
    while maxHeap:
        val, key = heappop(maxHeap)
        freq =  val
        for i in range(freq):
            ans.append(key)
    print(ans)
        

sortfreq(nums)