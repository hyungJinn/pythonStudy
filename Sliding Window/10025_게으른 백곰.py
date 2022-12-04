# https://www.notion.so/10025_-py-c7a2e7e562104afc9d0e4c254821b7f8

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
zoo = [list(map(int, input().split())) for _ in range(N)]

arr = [0 for _ in range(1000001)] # target's place
for i in range(N):
    arr[zoo[i][1]] = zoo[i][0]

step = K * 2 + 1
tmp = sum(arr[:step])
result = tmp

for i in range(step, 1000001):
    tmp += arr[i] - arr[i - step]
    result = max(result, tmp)
    
print(result)