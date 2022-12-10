# https://jokerldg.github.io/algorithm/2021/11/19/turret.html
# https://www.notion.so/1002_-py-9da1ac90ac87491596e366fbca06751a

import sys
import math
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == distance or (r1+r2) == distance:
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):
        print(2)
    else:
        print(0)