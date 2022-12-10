# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(x, y, h-y, w-x))