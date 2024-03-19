from heapq import *
words = ["i","love","leetcode","i","love","coding"]
k = 2

def topK(words, k):
    mp = {}
    for i in words:
        mp[i] = mp.get(i, 0)+1
    
    # print(mp)
    maxHeap = []
    for key, value in mp.items():
        heappush(maxHeap, (-value, key))
    res = []
    for i in range(k):
        res.append(heappop(maxHeap)[1])
    print(res)
topK(words, k)