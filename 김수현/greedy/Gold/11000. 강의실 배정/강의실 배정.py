import sys, heapq

n = int(input())

data = []
cnt = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append([a, b])

data.sort()

heap = []
heapq.heappush(heap, data[0][1])

for i in range(1, n):
    if (data[i][0] >= heap[0]):
        heapq.heappop(heap)
    heapq.heappush(heap, data[i][1])

print(len(heap))
