# https://wook-2124.tistory.com/246

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)