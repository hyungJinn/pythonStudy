# 2675_문자열 반복.py

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().split()
    result = ''
    for s in S:
        result += s * int(R)
    print(result)