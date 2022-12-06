# https://www.notion.so/10814_-py-18b4fb547db24c6d9bacf53c35bb9a0f

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    age, name = map(str, input().split())
    arr.append([int(age), i, name])

result = sorted(arr) # sorted array

for i in range(N):
    print(result[i][0], result[i][2]) # [age, index, name]