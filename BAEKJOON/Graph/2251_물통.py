import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())

def pour(x, y):
    if not visit[x][y]:
        visit[x][y] = True
        q.append([x, y])
        

def bfs():
    # bfs 시작!
    q.append([0, 0])
    visit[0][0] = True
    
    while q:
        x, y = q.popleft()
        z = C - x - y
        if x == 0:
            ans.append(z)
        
        # x -> y
        water = min(x, B - y)
        pour(x - water, y + water)
        
        # x -> z
        water = min(x, C - z)
        pour(x - water, y)
        
        # y -> x
        water = min(y, A - x)
        pour(x + water, y- water)
        
        # y -> z
        water = min(y, C - z)
        pour(x, y - water)
        
        # z -> x
        water = min(z, A - x)
        pour(x + water, y)
        
        # z -> y
        water = min(z, B - y)
        pour(x, y + water)
        

q = deque()
ans = []

visit = [[False] * (B + 1) for _ in range(A + 1)]
bfs()

ans.sort()
print(' '.join(map(str, ans)))
