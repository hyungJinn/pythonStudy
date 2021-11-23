import sys

N, K = map(int, sys.stdin.readline().split())

result = 0
arr = []

for i in range(0, N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in arr:
    if K >= i:
        result += K // i
        K = K % i
    
    if K == 0:
        break

print(result)