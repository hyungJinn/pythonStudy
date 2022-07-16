#1389_kavinbacon_6levelofrules

"""
DFS를 사용하면 카운트 개수 때문에 복잡해질 수 있어서 BFS로 풀었다.
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
  num = [0] * (N + 1)
  visited = [start]
  queue = deque()
  queue.append(start)

  while queue:
    a = queue.popleft()
    for i in graph[a]:
      if i not in visited:
        num[i] = num[a] + 1 
        visited.append(i)
        queue.append(i)

  return sum(num)

N, M = map(int, input().split())

# 노드 범위가 1~N이니까 N+1
graph = [[] for _ in range(N+1)]

# 양방향 그래프 생성
for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# print(graph)

result = []
for i in range(1, N+1):
  result.append(bfs(graph, i))

print(result.index(min(result))+1)