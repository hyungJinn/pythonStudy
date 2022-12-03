# https://www.notion.so/2167_2-py-99b73e93187346b2abc12b2789961dd8

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (M + 1)]

for _ in range(N):
    xy = [0] + [int(x) for x in input().split()]
    arr.append(xy)
    
for i in range(1, N + 1):
    for j in range(1, M):
        arr[i][j + 1] += arr[i][j]

for j in range(1, M + 1):
    for i in range(1, N):
        arr[i + 1][j] += arr[i][j]
        
K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])