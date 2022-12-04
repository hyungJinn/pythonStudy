# https://www.notion.so/2559_-py-ddc3b5595db84904aded64d8e3db4540

import sys
input = sys.stdin.readline

# K = continuous date
N, K = map(int, input().split())
arr = list(map(int, input().split()))

tmp = sum(arr[:K])
result = tmp
for i in range(K, N):
    tmp += arr[i] - arr[i-K]
    result = max(result, tmp)

print(result)