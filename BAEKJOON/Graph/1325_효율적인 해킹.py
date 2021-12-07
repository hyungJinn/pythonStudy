import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


def bfs(v):
    D = 0
    q = deque()
    q.append(v)
    
    visit = [False] * (N + 1)
    visit[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = True
                q.append(i)
                D += 1
    return D


for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_value = 0
result = []
for i in range(1, N + 1):
    if graph[i]:
        temp = bfs(i)
        if max_value < temp:
            max_value = temp
            result = [i]
        elif max_value == temp:
            result.append(i)

print(*result)