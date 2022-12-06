# https://www.notion.so/11651_-2-py-79b33cfd9cd040e9bad66f84f91abb4d

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([y, x]) # only difference from 11650_좌표 정렬하기.py

result = sorted(arr)

for i in range(N):
    print(result[i][1], result[i][0]) # [y, x]