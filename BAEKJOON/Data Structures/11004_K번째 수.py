import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
nums = list(map(int, input().split()))

heapq.heapify(nums)

for _ in range(K):
    result = heapq.heappop(nums)

print(result)

