import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

sum = 0
for i in range(0, N):
    temp = 0
    for j in range(0, i + 1):
        temp += int(arr[j])
    sum += temp

print(sum)