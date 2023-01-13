# https://kjhoon0330.tistory.com/entry/BOJ-2075-N%EB%B2%88%EC%A7%B8-%ED%81%B0-%EC%88%98-Python

import sys
input = sys.stdin.readline
import heapq

heap = []
N = int(input())

for _ in range(N):
    nums = map(int, input().split())
    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
print(heap[0])