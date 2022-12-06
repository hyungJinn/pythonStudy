# https://www.notion.so/11650_-py-5af7d7c3087745a0a3be4b7597673407

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
# print(arr)

result = sorted(arr) # sorted array

for i in range(N):
    print(result[i][0], result[i][1])
