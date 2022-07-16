import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end):
  visited = [0 for i in range(N+1)]
  queue = deque()
  queue.append(start)
  while queue:
    x, y = queue.popleft()
    if abs(x - end[0]) + abs(y - end[1]) <= 1000:
      print("happy")
      return
    for i in range(N):
      if not visited[i]:
        nx, ny = store[i]
        if abs(x - nx) + abs(y - ny) <= 1000:
          queue.append([nx, ny])
          visited[i] = 1
  print("sad")
  return

TC = int(input())
for i in range(TC):
  N = int(input())
  x0, y0 = map(int, input().split())
  store = []
  for j in range(N):
    x, y = map(int, input().split())
    store.append([x, y])
  x1, y1 = map(int, input().split())
  bfs([x0, y0], [x1, y1])